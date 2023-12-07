"""
Algorithm is based on Computerphile's video: https://youtu.be/G_UYXzGuqvM?si=vRvoPj-npqoSkux1

"""

from export import import_json, TEST_1, TEST_2, HAND_WRITTEN

grid: list[list[int]] = None

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


def brute_force(sol_count: int = 0) -> int:
    """
    Do no directly use this function. Use solve() instead.
    """
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for t in range(1, 10):
                    if is_possible(x, y, t):
                        grid[y][x] = t
                        sol_count = brute_force(sol_count=sol_count)
                        grid[y][x] = 0
                return sol_count
    print(f'Solution #{sol_count + 1}')
    for row in grid:
        print(row)
    print()
    return sol_count + 1


def solve(_grid: list[list[int]] = None) -> int:
    """
    Wrapper to use brute_force() function.
    Returns the number of solutions.
    """
    global grid
    grid = _grid
    return brute_force()



def main():
    grid = import_json(TEST_2)
    solution_count = solve(grid)
    print(f'Total solutions: {solution_count}')
    
    for row in grid:
        print(row)
    print()

    



if __name__ == '__main__':
    main()