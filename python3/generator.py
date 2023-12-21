"""
Sudoku is a puzzle that is easily cracked with brute force approach.

First things that comes to mind to create a generator algorithm,
is to randomly fill the grid with numbers, then randomly remove numbers
and check if it is still solvable.

For deciding difficulty, we can use the iteration count of the algorithm.
"""

""" --DEPRECATED--
def fill_random_grid() -> list[list[int]]:
    global _grid
    _grid = [[0 for _ in range(9)] for _ in range(9)]
    for t in range(3):
        remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(remaining)
        for y in range(3):
            for x in range(3):
                random_choice = choice(remaining)
                _grid[y + t * 3][x + t * 3] = random_choice
                remaining.remove(random_choice)
    
    for square in [(0, 2), (2, 0)]:
        remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(3):
            for i in range(3):
                while True:
                    t = choice(remaining)
                    cursor = (square[0] * 3 + i, square[1] * 3 + j)
                    if is_possible(cursor[0], cursor[1], t):
                        _grid[cursor[1]][cursor[0]] = t
                        remaining.remove(t)
                        break
    for row in _grid:
        print(row)
    return _grid
"""
""" --DEPRECATED--
def brute_force_fill() -> None:
    global _grid
    cell_input = [i for i in range(81)]
    shuffle(cell_input)
    for i in range(50):
        cell = cell_input.pop()
        x = cell % 9
        y = cell // 9
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(nums)
        while len(nums) > 0:
            t = nums.pop()
            if _grid[y][x].t == 0 and _grid[y][x].possibles:
                add_number(x, y, t)
 """
""" --DEPRECATED--
def is_possible(x: int, y: int, t: int) -> bool:
    #x: x coordinate
    #y: y coordinate
    #t: number to be tested
    assert x >= 0 and x < 9 and int(x) == x, f'x is out of range: {x}'
    assert y >= 0 and y < 9 and int(y) == y, f'y is out of range: {y}'
    assert t > 0 and t <= 9 and int(t) == t, f't is out of range: {t}'
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
"""


from random import randint, shuffle, choice
from solver import solve, solve_and_count
from export import save_json, import_json, TEST_DIR
from visualiser import draw_grid
from copy import deepcopy


_grid: list[list[int]] = None
_possibilities: list[list[list[int]]] = None
_empty_cells: list[tuple[int, int]] = None


def collect_garbage(function_to_decorate):
    def wrapper(*args, **kw):
        output = function_to_decorate(*args, **kw)
        global _grid, _possibilities, _empty_cells
        _grid = None
        _possibilities = None
        _empty_cells = None
        return output
    return wrapper 


def put_number(x: int, y: int, t: int) -> None:
    """
    x: x coordinate
    y: y coordinate
    t: number to be tested
    """
    assert x >= 0 and x < 9 and int(x) == x, f'x is out of range: {x}'
    assert y >= 0 and y < 9 and int(y) == y, f'y is out of range: {y}'
    assert t >= 0 and t <= 9 and int(t) == t, f't is out of range: {t}'
    global _grid, _possibilities, _empty_cells
    _grid[y][x] = t
    _possibilities[y][x] = []
    _empty_cells.remove((x, y))
    # for the row, column and square, remove t from possibilities if it exists
    for i in range(9):
        if t in _possibilities[y][i]:
            _possibilities[y][i].remove(t)
        if t in _possibilities[i][x]:
            _possibilities[i][x].remove(t)
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if t in _possibilities[y0 + i][x0 + j]:
                _possibilities[y0 + i][x0 + j].remove(t)


def fill_diagonal() -> list[list[int]]:
    global _grid
    _grid = [[0 for _ in range(9)] for _ in range(9)]
    for t in range(3):
        remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(remaining)
        for y in range(3):
            for x in range(3):
                random_choice = choice(remaining)
                put_number(x + t * 3, y + t * 3, random_choice)
                remaining.remove(random_choice)
    return _grid


def get_single_cells() -> list[tuple[int, int, int]]:
    global _possibilities
    output = []
    for y in range(9):
        for x in range(9):
            if len(_possibilities[y][x]) == 1:
                output.append((x, y, _possibilities[y][x][0]))
    return output


def is_completed() -> bool:
    global _grid
    for row in _grid:
        for cell in row:
            if cell == 0:
                return False
    return True


def fill_remaining() -> None:
    global _grid, _possibilities, _empty_cells
    while not is_completed():
        single_cells = get_single_cells()
        if len(single_cells) == 0:
            selected_cell = choice(_empty_cells)
            t = choice(_possibilities[selected_cell[1]][selected_cell[0]])
            put_number(selected_cell[0], selected_cell[1], t)
        else:
            for cell in single_cells:
                put_number(cell[0], cell[1], cell[2])
    

@collect_garbage
def generate() -> list[list[int]]:
    global _grid, _possibilities, _empty_cells
    _grid = [[0 for _ in range(9)] for _ in range(9)]
    _possibilities = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]
    _empty_cells = [(x, y) for x in range(9) for y in range(9)]
    fill_diagonal()
    fill_remaining()
    return deepcopy(_grid)


def main():
    grid = generate()
    for row in grid:
        print(row)
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if _grid is not None:
            draw_grid(_grid)
    except Exception as e:
        print(e)
        if _grid is not None:
            draw_grid(_grid)
    





