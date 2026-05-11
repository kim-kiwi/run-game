import pygame
import sys
import background_logic

pygame.init()

width,height=1300,1000

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Hello from Python!")

background_logic.init(width,height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    background_logic.do(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
