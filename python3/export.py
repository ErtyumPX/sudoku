import json
import os

ABS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = ABS_DIR + '/test_data'
TEST_1 = TEST_DIR + '/puzzle_test.json'
TEST_2 = TEST_DIR + '/test_2.json'
HAND_WRITTEN = TEST_DIR + '/hand_written.json'


"""
JSON Format
-----------

For testing:
{ 'grid': list[list[int]] }

For future:
{ 'grid': list[list[int]], 'solution': list[list[int]] }
"""

OVERRIDE_TEXT = "WARNING: File already exists at '{0}'!\nDo you want to override? (Y/n): "
def save_json(path: str, grid: list[list[int]]) -> None:
    if os.path.exists(path):
        answer = input(str.format(OVERRIDE_TEXT, path)).lower()
        if answer == 'n' or answer == 'q':
            return
    with open(path, 'w') as f:
        data = {
            'grid': grid
        }
        json.dump(data, f)


def import_json(path: str) -> list[list[int]]:
    assert os.path.exists(path), f'File not found: {path}'
    with open(path, 'r') as f:
        data = json.load(f)
    return data['grid']


def main():
    grid = [[2,0,9,3,5,6,0,0,0],
            [0,0,0,0,7,0,0,0,0],
            [7,1,0,2,0,0,0,0,0],
            [0,4,2,0,0,0,0,9,7],
            [8,9,0,0,0,0,0,6,3],
            [3,5,0,0,0,0,1,4,0],
            [0,0,0,0,0,7,0,3,4],
            [0,0,0,0,2,0,0,0,0],
            [0,0,0,1,4,3,7,0,9]]
    save_json(TEST_DIR + "/hand_written.json", grid)


if __name__ == '__main__':
    main()