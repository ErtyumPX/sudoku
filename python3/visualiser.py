from export import import_json
import pygame
import os



ABS_DIR: str = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FONT_PATH: str = ABS_DIR + '/data/SpaceMono-Regular.ttf'



def grid_to_surface(root: pygame.Surface, grid: list[list[int]]) -> None:
    """
    Draws the background grid, bridges and islands to the passed surface.
    """
    pygame.init()
    cell_unit = root.get_size()[0] // 9
    font: pygame.font.Font = pygame.font.Font(DEFAULT_FONT_PATH, int(cell_unit / 2))
    root_size = root.get_size()

    # draw the grid
    line_thickness = cell_unit // 10
    root.fill((255, 255, 255))
    for i in range(10):
        thickness_factor = 2 if i % 3 == 0 else 1
        pygame.draw.line(root, (220, 220, 220), (i * cell_unit, 0), (i * cell_unit, root_size[1]), line_thickness * thickness_factor)
    for j in range(10):
        thickness_factor = 2 if j % 3 == 0 else 1
        pygame.draw.line(root, (220, 220, 220), (0, j * cell_unit), (root_size[0], j * cell_unit), line_thickness * thickness_factor)

    for x in range(9):
        for y in range(9):
            if grid[y][x] != 0:
                text = font.render(str(grid[y][x]), True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (x * cell_unit + cell_unit // 2, y * cell_unit + cell_unit // 2)
                root.blit(text, text_rect)


def draw_grid(grid: list[list[int]]) -> None:
    pygame.init()
    SIZE: tuple(int, int) = (630, 630)
    UNIT: int = SIZE[0] // 9
    root: pygame.Surface = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Sudoku Visualiser')
    for x in range(9):
        for y in range(9):
            pass
    loop: bool = True
    while loop:
        ALL_EVENTS: list[pygame.event.Event] = pygame.event.get()
        for event in ALL_EVENTS:
            if event.type == pygame.QUIT:
                loop = False
        grid_to_surface(root, grid)
        pygame.display.update()


def parse_args() -> list[list[int]]:
    pass


def main():
    grid = import_json("test_data/hand_written.json")
    draw_grid(grid)


if __name__ == '__main__':
    main()
