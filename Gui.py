import pygame
import sys
import Board
import Ai
import time

pygame.init()
pygame.font.init()



black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)


width = 700
height = 950
radius = 40

screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption("Connect four")


myFont = pygame.font.SysFont("arial", 30, bold=True)


restartButton = pygame.Rect(540, 20, 140, 170)
scorePanel = pygame.Rect(20, 20, 500, 60)
timePanel = pygame.Rect(20, 115, 500, 60)
levelPanel = pygame.Rect(110, 801,460, 50)
subLevelPanel = myFont.render("Poziom trudności (zagłębienie)", True, white)
pygame.draw.rect(screen, black, levelPanel)
screen.blit(subLevelPanel, (120, 807))


ai_depth = 2
lev_array = []

for i in range(8):

    lev_rect = pygame.Rect(20 + 86*i, 880, 50, 50)
    lev_array.append((lev_rect, i+1))



pygame.draw.rect(screen, blue, restartButton)
pygame.draw.rect(screen, blue, scorePanel)
pygame.draw.rect(screen, blue, timePanel)
sub = myFont.render("Restart", True, white)
timeSub = myFont.render("Czas myślenia bota: ", True, white)
screen.blit(sub, (555, 35))
screen.blit(timeSub, (35, 130))


myBoard = Board.createBoard()
show_message = False

def draw_board(board):
    pygame.draw.rect(screen, blue, scorePanel)
    for lev_rect, level in lev_array:
        theColor = red if ai_depth == level else blue
        pygame.draw.rect(screen, theColor, lev_rect)
        sub_for_level = myFont.render(str(level), True, white)
        screen.blit(sub_for_level, (37+86*(level-1), 887))
    for c in range(7):
        for r in range(6):
            # Parametry: (ekran, kolor, (X, Y, szerokość, wysokość))
            pygame.draw.rect(screen, blue, (c * 100, (r+2) * 100, 90, 90))

            if board[r][c] == 1:
                color = red
            elif board[r][c] == 2:
                color = yellow
            else:
                color = black

            # Parametry: (ekran, kolor, (środek_X, środek_Y), promień)
            center_x = int(c*100 + 45)
            center_y = int((r+2) * 100 + 45)

            pygame.draw.circle(screen, color, (center_x, center_y), radius)
    
    pygame.display.update()

draw_board(myBoard)

running = True
turn = 1
winner = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            if restartButton.collidepoint(event.pos) or winner is not None:
                winner = None
                show_message = False
                myBoard = Board.createBoard()
                turn = 1
                pygame.draw.rect(screen, blue, timePanel)
                screen.blit(timeSub, (35, 130))
                draw_board(myBoard)
                continue 

            if turn == 1:
                button_clicked = False
                for lev_rect, level in lev_array:
                    if lev_rect.collidepoint(event.pos):
                        ai_depth = level
                        button_clicked = True
                        draw_board(myBoard)
                        break

                if button_clicked:
                    continue
                        
            
            if turn == 1 and not (restartButton.collidepoint(event.pos)):
                posX = event.pos[0]
                col = int (posX // 100)

                if Board.is_valid_location(myBoard, col):
                    Board.drop_piece(myBoard, col, turn)
                    draw_board(myBoard)

                    if Board.check_win(myBoard, turn):
                        winner = turn
                        show_message = True
                    turn = 2

    if turn == 2 and winner is None:
        pygame.draw.rect(screen, blue, timePanel)
        screen.blit(timeSub, (35, 130))
        pygame.display.update()
        valid_loc = [c for c in range(7) if Board.is_valid_location(myBoard, c)]

        if valid_loc:
            start_time = time.time()
            best_col = Ai.get_best_move(myBoard,ai_depth)
            end_time = time.time()
            think_time = end_time - start_time
            subTime2 = myFont.render(f"{think_time:.3f} s", True, white)
            screen.blit(subTime2, (360, 130))
            Board.drop_piece(myBoard, best_col, turn)
            draw_board(myBoard)
            if Board.check_win(myBoard, turn):
                winner = turn
                show_message = True
            turn = 1
        else:
            winner = 0
            show_message = True

    if show_message:
        if winner == 1:
            text = "Wygrana"
        elif winner == 2:
            text = "Przegrana"
        else:
            text = "Remis"
        info = myFont.render(text, True, white)
        screen.blit(info, (200, 35))
        pygame.display.update()

        show_message = False

        

pygame.quit()
sys.exit()