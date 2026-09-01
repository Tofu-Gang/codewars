__author__ = "Tofu-Gang"
__email__ = "tofugangsw@gmail.com"

"""
https://www.codewars.com/kata/52423db9add6f6fc39000354

Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives on to the next generation.
4. Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in 
both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return 
value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively (PHP: plain black and white 
squares).
"""

from conways_game_of_life import ConwaysGameOfLife

def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    """
    :param cells: input cells map
    :param generations: generations count to run
    :return: cells map, cropped around all the living cells, after given number of generations
    """

    game = ConwaysGameOfLife(cells)
    game.run_generations(generations)
    return game.cells
