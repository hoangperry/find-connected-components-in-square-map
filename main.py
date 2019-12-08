import pygame
from algorithm import GraphAdjMatrix, GraphAdjList


class SquareMap:
    def __init__(self, board_width: int, board_height: int, cellsize: int = 40):
        pygame.init()
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', cellsize)
        self.board_width = board_width
        self.board_height = board_height
        self.board = [[0 for i in range(board_width)] for i in range(board_height)]
        self.cellsize = cellsize
        self.windows_width = cellsize * board_width
        self.windows_height = cellsize * board_height
        self.game_display = pygame.display.set_mode((self.windows_width, self.windows_height))
        self.graph = GraphAdjList()
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

    def display_component(self):
        self.graph.update_graph(self.board)
        list_component = self.graph.find_list_connected_component(algorithm='dfs')
        for index, components in enumerate(list_component):
            for component in components:
                pos_component = [int(i) for i in component.split('_')]
                self.display_num(index, pos_component[0], pos_component[1])

    def display_num(self, num_to_show, _x_pos, _y_pos):
        textsurface = self.myfont.render(str(num_to_show), False, (0, 0, 0))
        self.game_display.blit(textsurface, (_x_pos * self.cellsize, _y_pos * self.cellsize))

    def loop(self):
        crashed = False
        self.game_display.fill(self.game_color['white'])
        self.display_map()
        pygame.display.update()
        while not crashed:
            is_something_new = False
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.update_pos(pygame.mouse.get_pos())
                    is_something_new = True
                if event.type == pygame.QUIT:
                    crashed = True

            if is_something_new:
                self.game_display.fill(self.game_color['white'])
                self.display_map()
                self.display_component()
                pygame.display.update()
            # self.display_num()


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
