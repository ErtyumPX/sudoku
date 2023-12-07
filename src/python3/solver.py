"""
Algorithm is based on Computerphile's YouTube video:
Python Sudoku Solver - Computerphile -> https://youtu.be/G_UYXzGuqvM?si=vRvoPj-npqoSkux1
It's mind blowingly simple dude!

Although:

Intense recursion depths require efficient usage of global variables,
rather than passing the same static arguments over and over again.
Good to keep in mind...

"""

from export import import_json, TEST_1, TEST_2, HAND_WRITTEN
from copy import deepcopy

_grid: list[list[int]] = None
_all_solutions: list[list[list[int]]] = None


def collect_garbage(function_to_decorate):
    def wrapper(*args, **kw):
        output = function_to_decorate(*args, **kw)
        _grid = None
        _all_solutions = None
        return output
    return wrapper


def is_possible(x: int, y: int, t: int) -> bool:
    """
    x: x coordinate
    y: y coordinate
    t: number to be tested
    """
    assert x >= 0 and x < 9 and int(x) == x, f'x is out of range: {x}'
    assert y >= 0 and y < 9 and int(y) == y, f'y is out of range: {y}'
    assert t >= 1 and t <= 9 and int(t) == t, f't is out of range: {t}'
    global _grid
    for i in range(9):
        if _grid[y][i] == t:
            return False
        if _grid[i][x] == t:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if _grid[y0 + i][x0 + j] == t:
                return False
    return True


def brute_force() -> list[list[int]]:
    """
    Do no directly use this function. Use solve() instead.
    """
    global _grid, _all_solutions
    for y in range(9):
        for x in range(9):
            if _grid[y][x] == 0:
                for t in range(1, 10):
                    if is_possible(x, y, t):
                        _grid[y][x] = t
                        brute_force()
                        _grid[y][x] = 0
                return
    _all_solutions.append(deepcopy(_grid))


@collect_garbage
def solve(grid: list[list[int]]) -> list[list[list[int]]]:
    """
    Wrapper to use brute_force() function.
    Returns a list of all solution grids.
    """
    global _grid, _all_solutions
    _grid = grid
    _all_solutions = []
    brute_force()
    return deepcopy(_all_solutions)


def main():
    grid = import_json(TEST_2)
    solutions: list[list[int]] = solve(grid)
    for i, solution in enumerate(solutions):
        print(f'Solution #{i + 1}')
        for row in solution:
            print(row)
        print()


if __name__ == '__main__':
    main()