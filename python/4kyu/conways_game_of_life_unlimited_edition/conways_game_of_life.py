__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

from typing import Tuple, List
from copy import deepcopy


class ConwaysGameOfLife:
    ALIVE = 1
    DEAD = 0

########################################################################################################################

    def __init__(self, initial_state):
        """
        Store initial cells map.
        """

        self._cells = initial_state

########################################################################################################################

    @property
    def cells(self) -> List[List[int]]:
        """
        :return: cells map
        """

        return self._cells

########################################################################################################################

    def run_generations(self, count: int) -> None:
        """
        Run [count] number of generations.

        :param count: generations count
        """

        if count > 0:
            for _ in range(count):
                self._new_generation()
        self._crop()

########################################################################################################################

    def print_cells(self):
        """
        Print cells map. Dead and alive cells will be represented as ░░ and ▓▓ blocks respectively.
        """

        print("\n".join(
            " ".join(tuple("▓▓" if cell == self.ALIVE else "░░" for cell in row))
            for row in self._cells))
        print()

########################################################################################################################

    def _embiggen(self) -> None:
        """
        Add new row and/or column to every side of the cell map where there is an alive cell. Checks if it is needed are
        in place, safe to call at any time.
        """

        if any(True if row[0] == self.ALIVE else False for row in self._cells):
            # add column to the left
            self._cells = list([self.DEAD] + row for row in self._cells)
        if any(True if row[-1] == self.ALIVE else False for row in self._cells):
            # add column to the right
            self._cells = list(row + [self.DEAD] for row in self._cells)
        if any(True if cell == self.ALIVE else False for cell in self._cells[0]):
            # add row to the top
            self._cells.insert(0, list(self.DEAD for _ in range(len(self._cells[0]))))
        if any(True if cell == self.ALIVE else False for cell in self._cells[-1]):
            # add row to the bottom
            self._cells.append(list(self.DEAD for _ in range(len(self._cells[0]))))

########################################################################################################################

    def _crop(self) -> None:
        """
        Crop the cells map around all living cells.
        """

        while True:
            if all(True if row[0] == self.DEAD else False for row in self._cells):
                # remove left column
                self._cells = list(row[1:] for row in self._cells)
            elif all(True if row[-1] == self.DEAD else False for row in self._cells):
                # remove right column
                self._cells = list(row[:-1] for row in self._cells)
            elif all(True if cell == self.DEAD else False for cell in self._cells[0]):
                # remove top row
                self._cells = self._cells[1:]
            elif all(True if cell == self.DEAD else False for cell in self._cells[-1]):
                # remove bottom row
                self._cells = self._cells[:-1]
            else:
                break

########################################################################################################################

    def _alive_neighbors_count(self, row: int, column: int) -> Tuple[int]:
        """
        :param row: cell row
        :param column: cell column
        :return: all neighbor cells of the cell in [row][column]
        """

        neighbors_coords = [[row - 1, column - 1], [row - 1, column], [row - 1, column + 1],
                            [row, column - 1], [row, column + 1],
                            [row + 1, column - 1], [row + 1, column], [row + 1, column + 1]]
        filtered_neighbors_coords = list(filter(
            lambda coords: 0 <= coords[0] < len(self._cells)
                           and 0 <= coords[1] < len(self._cells[0]),
            neighbors_coords))
        return tuple(self._cells[coords[0]][coords[1]] for coords in filtered_neighbors_coords)

########################################################################################################################

    def _will_stay_alive(self, row: int, column: int) -> bool:
        """
        :param row: cell row
        :param column: cell column
        :return: True if the cell [row][column] will stay/become alive, False if it dies/stays dead, according to the
        game rules
        """

        alive_neighbors_count = self._alive_neighbors_count(row, column).count(self.ALIVE)
        cell = self._cells[row][column]

        # 1. Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
        # 2. Any live cell with more than three live neighbors dies, as if by overcrowding.
        # 3. Any live cell with two or three live neighbors lives on to the next generation.
        # 4. Any dead cell with exactly three live neighbors becomes a live cell.
        return ((cell == self.ALIVE and 2 <= alive_neighbors_count <= 3)
                or (cell == self.DEAD and alive_neighbors_count == 3))

########################################################################################################################

    def _new_generation(self) -> None:
        """
        Create new generation of cells, according to the game rules
        """

        self._embiggen()
        cells_copy = deepcopy(self._cells)

        for row in range(len(self._cells)):
            for column in range(len(self._cells[row])):
                cells_copy[row][column] = self.ALIVE if self._will_stay_alive(row, column) else self.DEAD

        self._cells = cells_copy
