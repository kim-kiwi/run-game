import pygame
import sys
import os
# logics
import background_logic
import player_logic
import test_spike
from utils import GameState
import ev

pygame.init()

width,height=1300,1000

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Hello from Python!")
current_path=os.path.dirname(__file__)

gameState=GameState(
    state=0,
    speed=15,
    font=pygame.font.Font(os.path.join(current_path,"malgun.ttf"), 48),
    width=width,
    height=height,
    plr=None
)
def reset():
    gameState.reset()
    background_logic.init(gameState)
    player_logic.init(gameState)
    test_spike.init(gameState)
reset()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))

    if gameState.state:
        background_logic.do(screen)
        player_logic.do(screen)
        test_spike.do(screen)
        gameState.speed+=0.005
    else:
        just_pressed_keys = pygame.key.get_just_pressed()
        if just_pressed_keys[pygame.K_SPACE]:
            reset()
            gameState.state=1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
