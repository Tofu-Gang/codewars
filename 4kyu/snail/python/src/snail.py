"""
Snail
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling
clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a
clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

from typing import List


########################################################################################################################

class Direction:
    """
    Class that manages current direction in the snail map. Based on that direction, it offers methods for next row and
    next column in the snail map. If necessary, the direction must be changed to the next one.

    It does not maintain any information about the snail map itself or the current position in it. Current position are
    supplied as params in the next row/column methods. It is not able to maintain the right direction by itself; the
    direction has to be switched manually by the respective method call.
    """

    _NEXT_ROW_KEY = "NEXT_ROW"
    _NEXT_COLUMN_KEY = "NEXT_COLUMN"

    _DIRECTIONS = ({  # right
                       _NEXT_ROW_KEY: lambda row: row,
                       _NEXT_COLUMN_KEY: lambda column: column + 1
                   }, {  # down
                       _NEXT_ROW_KEY: lambda row: row + 1,
                       _NEXT_COLUMN_KEY: lambda column: column
                   }, {  # left
                       _NEXT_ROW_KEY: lambda row: row,
                       _NEXT_COLUMN_KEY: lambda column: column - 1
                   }, {  # up
                       _NEXT_ROW_KEY: lambda row: row - 1,
                       _NEXT_COLUMN_KEY: lambda column: column
                   })

########################################################################################################################

    def __init__(self):
        """
        Start with the RIGHT direction.
        """

        self._index = 0

########################################################################################################################

    def change_direction(self) -> None:
        """
        Switch to the next snail direction (RIGHT, DOWN, LEFT, UP and so on).
        """

        self._index += 1
        self._index %= len(self._DIRECTIONS)

########################################################################################################################

    def next_row(self, row: int) -> int:
        """
        :param row: current row index in the snail map
        :return: next row index after moving in the current direction
        """

        return self._DIRECTIONS[self._index][self._NEXT_ROW_KEY](row)

########################################################################################################################

    def next_column(self, column: int) -> int:
        """
        :param column: current column index in the snail map
        :return: next column index after moving in the current direction
        """

        return self._DIRECTIONS[self._index][self._NEXT_COLUMN_KEY](column)


########################################################################################################################


class Snail:
    """
    Class that maintains the snail map and current position in it. It uses an instance of Direction class that provides
    next row/column indexes for movement. Element from the snail map is returned after every movement. Also, elements
    are deleted from the snail map and replaced by None after reading and returning them. This provides conditions for
    changing the direction: either the edge of the snail map is reached, or a previously read element is reached (None).
    """

    def __init__(self, snail_map: List[List[int]]):
        """
        Load the snail map and save its dimensions. Create an instance of direction management. Start just OUTSIDE the
        snail map, right before moving to the RIGHT on the top left element.
        """

        self._snail_map = snail_map
        self._WIDTH = len(self._snail_map[0])
        self._HEIGHT = len(self._snail_map)
        self._direction = Direction()
        self._row = 0
        # start just OUTSIDE the snail map
        self._column = -1

########################################################################################################################

    @property
    def next_element(self) -> int:
        """
        Move to the next element in the snail map and clear the previous one (replace with None).

        :return: next element in the snail map
        """

        # only look what is next in the current direction
        next_row = self._direction.next_row(self._row)
        next_column = self._direction.next_column(self._column)

        if next_row >= self._HEIGHT or next_column >= self._WIDTH or self._snail_map[next_row][next_column] is None:
            # it is necessary to change direction; either edge of the snail map or previously read element (None) would
            # be reached
            self._direction.change_direction()
            next_row = self._direction.next_row(self._row)
            next_column = self._direction.next_column(self._column)

        # now we can be sure that we stay in the snail map and previously unread element will be reached, make the move
        self._row = next_row
        self._column = next_column
        # store the new element for returning
        element = self._snail_map[self._row][self._column]
        # delete the current element
        self._snail_map[self._row][self._column] = None
        return element

########################################################################################################################

    @property
    def is_fully_searched(self) -> bool:
        """
        :return: True if all elements in the snail map were read and removed (all is None), False otherwise
        """

        return all(all(element is None for element in row) for row in self._snail_map)


########################################################################################################################


def snail(snail_map):
    """
    :param snail_map: 2D list with integers
    :return: elements read in a snail fashion (RIGHT, DOWN, LEFT, UP and so on)
    """

    snail = Snail(snail_map)
    result = []

    while not snail.is_fully_searched:
        # read the map until fully searched
        result.append(snail.next_element)

    return result
