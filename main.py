import pygame


class SquareMap:
    def __init__(self, board_width: int, board_height: int, cellsize: int = 40):
        pygame.init()
        self.board_width = board_width
        self.board_height = board_height
        self.board = [[0 for i in range(board_width)] for i in range(board_height)]
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

    def display_map(self):
        for i in range(self.board_width):
            for j in range(self.board_height):
                if (i + j) % 2 == 0:
                    if self.board[j][i] == 0:
                        background_color = self.game_color['gray']
                    else:
                        background_color = self.game_color['red']

                else:
                    if self.board[j][i] == 0:
                        background_color = self.game_color['white']
                    else:
                        background_color = self.game_color['dark_red']
                pygame.draw.rect(self.game_display, background_color,
                                 [i * self.cellsize, j * self.cellsize,
                                  self.cellsize, self.cellsize])

    def update_pos(self, pos):
        change_x_pos = pos[0]//self.cellsize
        change_y_pos = pos[1]//self.cellsize
        self.board[change_y_pos][change_x_pos] = 0 if self.board[change_y_pos][change_x_pos] == 1 else 1
        print(self.board[change_y_pos][change_x_pos])

    def loop(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_pos(pygame.mouse.get_pos())
                if event.type == pygame.QUIT:
                    crashed = True

            self.game_display.fill(self.game_color['white'])
            self.display_map()
            # self.display_num()
            pygame.display.update()


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
