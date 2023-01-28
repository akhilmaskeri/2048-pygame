import sys
import pygame
from board import Board

class BoardGui():

    def __init__(self, board):

        self.b = board

        pygame.init()
        pygame.display.set_caption("2048")

        self.screen = pygame.display.set_mode((405, 405))
        self.screen.fill((255, 255, 255))

    def update_board(self):

        white = (255,255,255)
        gray = (100,100,100)

        for i in range(4):
            for j in range(4):
                startx, starty = 5+100*i, 5+100*j
                pygame.draw.rect(self.screen, white, pygame.Rect(startx, starty, 95, 95), 0)
                pygame.draw.rect(self.screen, gray, pygame.Rect(startx, starty, 95, 95), 1)

        for i in range(4):
            for j in range(4):
                number = str(self.b.board[i][j] if self.b.board[i][j] > 0 else "  ")
                text_length = len(number)

                font = pygame.font.SysFont('timesnewroman', 30)
                text = font.render(number, True, (100,100,100),(255,255,255))
                self.screen.blit(text, ((100*(i+1))-(45+(10*text_length)), (100*(j+1))-65))

        pygame.display.update()

    def game_over(self):
        print("Game over called")
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('timesnewroman', 30)
        text = font.render("Game Over", True, (255, 255, 255),(0,0,0))
        self.screen.blit(text, (127, 187))
        pygame.display.update()
        
    
    def loop(self):

        running = True

        self.b.generate()
        self.update_board()

        press_complete = True
        moved = False

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                
                if event.type == pygame.KEYUP:

                    press_complete = True

                    if not self.b.possible_move_condition():
                        self.game_over()

                    if moved:
                        self.b.generate()
                        self.update_board()
                        moved = False
                    
            key_input = pygame.key.get_pressed()

            if press_complete and key_input[pygame.K_LEFT]:
                moved = self.b.up()
                press_complete = False

            if press_complete and key_input[pygame.K_RIGHT]:
                moved = self.b.down()
                press_complete = False

            if press_complete and key_input[pygame.K_UP]:
                moved = self.b.left()
                press_complete = False

            if press_complete and key_input[pygame.K_DOWN]:
                moved = self.b.right()
                press_complete = False

if __name__ == "__main__":
    b = BoardGui()
    b.draw()