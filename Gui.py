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
myFont2 = pygame.font.SysFont("arial", 18, bold=True)


restartButton = pygame.Rect(540, 20, 140, 60)
scorePanel = pygame.Rect(20, 20, 500, 60)
timePanel = pygame.Rect(20, 85, 660, 60)
levelPanel = pygame.Rect(110, 746 ,460, 50)
algorithm_panel = pygame.Rect(110, 855, 460, 40)
pygame.draw.rect(screen, black, algorithm_panel)
sub_algorithm_panel = myFont.render("Algorytm myślenia bota", True, white)
screen.blit(sub_algorithm_panel, (170, 856))

algorithm_array = []
algorithm_minimax = pygame.Rect(360, 900 ,210, 40)
algorithm_minimax_alfa_beta = pygame.Rect(110, 900, 210, 40)
sub_algorithm_minimax = myFont2.render("MINIMAX", True, white)
sub_algorithm_minimax_alfa_beta = myFont2.render("MINIMAX_ALFA_BETA", True, white)


screen.blit(sub_algorithm_minimax, (424, 910))
screen.blit(sub_algorithm_minimax_alfa_beta, (119, 910)) #DOBRZE
algorithm_array.append((algorithm_minimax, 1))
algorithm_array.append((algorithm_minimax_alfa_beta, 2))

subLevelPanel = myFont.render("Poziom trudności (zagłębienie)", True, white)
pygame.draw.rect(screen, black, levelPanel)
screen.blit(subLevelPanel, (120, 755))

algorithm_choice = 1
ai_depth = 2
lev_array = []

for i in range(8):

    lev_rect = pygame.Rect(20 + 86*i, 800, 50, 50)
    lev_array.append((lev_rect, i+1))



pygame.draw.rect(screen, blue, restartButton)
pygame.draw.rect(screen, blue, scorePanel)
pygame.draw.rect(screen, blue, timePanel)
sub = myFont.render("Restart", True, white)
timeSub = myFont.render("Czas myślenia bota: ", True, white)
screen.blit(sub, (555, 35))
screen.blit(timeSub, (35, 100))


myBoard = Board.createBoard()
show_message = False

def draw_board(board):
    pygame.draw.rect(screen, blue, scorePanel)
    for lev_rect, level in lev_array:
        theColor = red if ai_depth == level else blue
        pygame.draw.rect(screen, theColor, lev_rect)
        sub_for_level = myFont.render(str(level), True, white)
        screen.blit(sub_for_level, (37+86*(level-1), 808))
    for algorithm_rect, choice in algorithm_array:
        rect_color = red if choice == algorithm_choice else blue
        pygame.draw.rect(screen, rect_color, algorithm_rect)
    screen.blit(sub_algorithm_minimax, (424, 910))
    screen.blit(sub_algorithm_minimax_alfa_beta, (119, 910))
    for c in range(7):
        for r in range(6):
            # Parametry: (ekran, kolor, (X, Y, szerokość, wysokość))
            pygame.draw.rect(screen, blue, (5 + c * 100, (r+2) * 100-50, 90, 90))

            if board[r][c] == 1:
                color = red
            elif board[r][c] == 2:
                color = yellow
            else:
                color = black

            # Parametry: (ekran, kolor, (środek_X, środek_Y), promień)
            center_x = int(5 + c*100 + 45)
            center_y = int((r+2) * 100 -5)

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
                screen.blit(timeSub, (35, 100))
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

            if turn == 1:
                button_clicked = False
                for algorithm_rect, choice in algorithm_array:
                    if algorithm_rect.collidepoint(event.pos):
                        algorithm_choice = choice
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
        screen.blit(timeSub, (35, 100))
        pygame.display.update()
        valid_loc = [c for c in range(7) if Board.is_valid_location(myBoard, c)]

        if valid_loc:
            start_time = time.time()
            best_col = Ai.get_best_move(myBoard, ai_depth, algorithm_choice)
            end_time = time.time()
            think_time = end_time - start_time
            subTime2 = myFont.render(f"{think_time:.3f} s", True, white)
            screen.blit(subTime2, (360, 100))
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