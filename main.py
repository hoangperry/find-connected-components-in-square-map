import pygame


class SquareMap:
    def __init__(self, board_width: int, board_height: int, cellsize: int = 40):
        pygame.init()
        self.board_width = board_width
        self.board_height = board_height
        self.cellsize = cellsize
        self.windows_width = cellsize * board_width
        self.windows_height = cellsize * board_height
        self.game_display = pygame.display.set_mode((self.windows_width, self.windows_height))
        self.clock = pygame.time.Clock()
        self.game_color = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 150, 150),
            'dark_red': (150, 0, 0),
            'gray': (120, 120, 120),
        }

    def loop(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
            self.game_display.fill(self.game_color['white'])
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    prog = SquareMap(board_width=10, board_height=10, cellsize=30)
    prog.loop()
    # pygame.init()
    # gameDisplay = pygame.display.set_mode((800, 600))
    # pygame.display.set_caption('A bit Racey')
    # crashed = False
    # clock = pygame.time.Clock()
    # while not crashed:
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             crashed = True
    #
    #         print(event)
    #
    #     pygame.display.update()
    #     clock.tick(60)
