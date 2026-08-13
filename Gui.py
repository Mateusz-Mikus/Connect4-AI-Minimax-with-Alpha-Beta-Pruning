import pygame
import sys

pygame.init()
pygame.font.init()



black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)


width = 700
height = 700
radius = 40

screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption("Connect four")


myFont = pygame.font.SysFont("arial", 30, bold=True)


restartButton = pygame.Rect(540, 20, 140, 60)
scorePanel = pygame.Rect(20, 20, 500, 60) 

pygame.draw.rect(screen, blue, restartButton)
sub = myFont.render("Restart", True, white)
screen.blit(sub, (555, 35))


def draw_board():

    for c in range(7):
        for r in range(6):
            # Parametry: (ekran, kolor, (X, Y, szerokość, wysokość))
            pygame.draw.rect(screen, blue, (c * 100, (r+1) * 100, 90, 90))

            color = black

            # Parametry: (ekran, kolor, (środek_X, środek_Y), promień)
            center_x = int(c*100 + 45)
            center_y = int((r+1) * 100 + 45)

            pygame.draw.circle(screen, color, (center_x, center_y), radius)
    
    pygame.display.update()

draw_board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()