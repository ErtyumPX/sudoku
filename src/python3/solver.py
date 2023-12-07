"""
Algorithm is based on Computerphile's video: https://youtu.be/G_UYXzGuqvM?si=vRvoPj-npqoSkux1

"""

from export import import_json, TEST_1, TEST_2

grid: list[list[int]] = None
solution_count = 0

def is_possible(x: int, y: int, t: int) -> bool:
    """
    x: x coordinate
    y: y coordinate
    t: number to be tested
    """
    assert x >= 0 and x < 9 and int(x) == x, f'x is out of range: {x}'
    assert y >= 0 and y < 9 and int(y) == y, f'y is out of range: {y}'
    assert t >= 1 and t <= 9 and int(t) == t, f't is out of range: {t}'
    global grid
    for i in range(9):
        if grid[y][i] == t:
            return False
        if grid[i][x] == t:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == t:
                return False
    return True


def solve(_grid: list[list[int]] = None) -> int:
    global grid, solution_count
    if _grid != None:
        grid = _grid
        solution_count = 0
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for t in range(1, 10):
                    if is_possible(x, y, t):
                        grid[y][x] = t
                        solve()
                        grid[y][x] = 0
                return
    solution_count += 1


def main():
    grid = import_json(TEST_1)
    solve(grid)
    global solution_count
    print(solution_count)

if __name__ == '__main__':
    main()