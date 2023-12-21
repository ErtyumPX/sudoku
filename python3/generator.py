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


from random import randint, shuffle, choice
from solver import solve, solve_and_count
from export import save_json, import_json, TEST_DIR
from copy import deepcopy


_grid: list[list[int]] = None
_columns: list[list[int]] = None
_boxes: list[list[list[int]]] = None


def collect_garbage(function_to_decorate):
    def wrapper(*args, **kw):
        output = function_to_decorate(*args, **kw)
        global _grid, _columns, _boxes
        _grid = None
        _columns = None
        _boxes = None
        return output
    return wrapper


def is_possible(x: int, y: int, t: int) -> bool:
    # y - 1 is because first row is auto-placed
    column_check =_columns[y].count(t) != 0
    box_check = _boxes[y // 3][x // 3].count(t) != 0
    return column_check and box_check

def add_number(x: int, y: int, t: int) -> None:
    """
    x: x coordinate
    y: y coordinate
    t: number to be tested
    """
    assert x >= 0 and x < 9 and int(x) == x, f'x is out of range: {x}'
    assert y >= 0 and y < 9 and int(y) == y, f'y is out of range: {y}'
    assert t >= 1 and t <= 9 and int(t) == t, f't is out of range: {t}'
    global _grid, _columns, _boxes
    _grid[y][x] = t
    _columns[y].remove(t)
    _boxes[y // 3][x // 3].remove(t)


def iterative_fill() -> None:
    global _grid
    first = [i for i in range(1, 10)]
    shuffle(first)
    for i in range(9):
        add_number(i, 0, first.pop())
    for j in range(1, 9):
        for i in range(0, 9):
            remaining = [i for i in range(1, 10)]
            shuffle(remaining)
            while len(remaining) > 0:
                t = remaining.pop()
                if is_possible(i, j, t):
                    add_number(i, j, t)
                    break
                elif len(remaining) == 0:
                    print(f'No possible number found for {i}x{j}!')
                    return


@collect_garbage
def generate() -> list[list[int]]:
    global _grid, _columns, _boxes
    _grid = [[0 for _ in range(9)] for _ in range(9)]
    _columns = [[i for i in range(1, 10)] for _ in range(9)]
    _boxes = [[[i for i in range(1, 10)] for _ in range(3)] for _ in range(3)]
    iterative_fill()
    for row in _grid:
        print(row)
    print()




def main():
    random_grid: list[list[int]] = generate()
    for row in random_grid:
        print(row)
    print()


if __name__ == '__main__':
    main()
    