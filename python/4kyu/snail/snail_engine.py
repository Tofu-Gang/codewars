__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import List, Union


class SnailEngine:

########################################################################################################################

    def __init__(self, snail_map: List[List[int]]):
        """
        :param snail_map: input matrix
        """

        # store the input matrix and list for the values read in snail order
        self._snail_map = snail_map
        self._result = []

        # store input matrix width and height
        self._width = len(self._snail_map[0])
        self._height = len(self._snail_map)

        # keep track of the current position in the matrix
        self._row = 0
        self._column = 0

        # store movement methods references in snail order (right, down, left, up)
        self._directions = (self._go_right, self._go_down, self._go_left, self._go_up)
        self._direction_index = 0

########################################################################################################################

    @property
    def current_value(self) -> Union[int|None]:
        """
        :return: element in the current position or None if the current position is out of bounds of the snail map
        """

        try:
            return self._snail_map[self._row][self._column]
        except IndexError:
            return None

########################################################################################################################

    def _clear_current(self) -> None:
        """
        Clear an element in the current position to mark it as read already.
        """

        self._snail_map[self._row][self._column] = None

########################################################################################################################

    def _move(self, backtrack=False) -> None:
        """
        Move to the next element in the current direction.

        :param backtrack: Move in the opposite direction if True
        """

        self._directions[self._direction_index](backtrack)

########################################################################################################################

    def _go_right(self, backtrack=False) -> None:
        """
        Move right to the next element.

        :param backtrack: Move left instead if True.
        """

        if backtrack:
            self._column -= 1
        else:
            self._column += 1

########################################################################################################################

    def _go_down(self, backtrack=False) -> None:
        """
        Move down to the next element.

        :param backtrack: Move up instead if True.
        """

        if backtrack:
            self._row -= 1
        else:
            self._row += 1

########################################################################################################################

    def _go_left(self, backtrack=False) -> None:
        """
        Move left to the next element.

        :param backtrack: Move right instead if True.
        """

        if backtrack:
            self._column += 1
        else:
            self._column -= 1

########################################################################################################################

    def _go_up(self, backtrack=False) -> None:
        """
        Move up to the next element.

        :param backtrack: Move down instead if True.
        """

        if backtrack:
            self._row += 1
        else:
            self._row -= 1

########################################################################################################################

    def make_snail_path(self):
        """
        Read the matrix in snail order.

        :return: all values from the matrix read in snail order
        """

        while len(self._result) < self._width * self._height:
            # until all values in the matrix are read

            if self.current_value:
                # current value wasn't read yet; add it to the result
                self._result.append(self.current_value)
                # clear it, which marks it as read already
                self._clear_current()
                # move to the next element
                self._move()
            else:
                # either we are out of bounds of the matrix, or the current element was already read; move back in the
                # opposite direction by one element
                self._move(backtrack=True)
                # change direction
                self._direction_index += 1
                self._direction_index %= len(self._directions)
                # move to the next element
                self._move()

        return self._result
