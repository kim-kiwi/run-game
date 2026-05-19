import pygame
from utils import Vector, draw_rect
import ev

class State:
    STAND=0
    SLIDE=1

PLR_SIZE_BY_STATE = {}
PLR_SIZE_BY_STATE[State.STAND]=Vector(100,200)
PLR_SIZE_BY_STATE[State.SLIDE]=Vector(200,100)
PLR_OFFSET_BY_STATE = {}
PLR_OFFSET_BY_STATE[State.STAND]=Vector(0,-PLR_SIZE_BY_STATE[State.STAND].y*0.5)
PLR_OFFSET_BY_STATE[State.SLIDE]=Vector(0,-PLR_SIZE_BY_STATE[State.SLIDE].y*0.5)
GROUND=800
MAX_HP=3
MAX_JMP=2
MAX_BOOST=10

class Player:
    def __init__(it):
        it.pos = Vector(300,GROUND)
        it.vel = Vector(0,0)
        it.state = State.STAND
        it.on_ground = False
        it.hp = MAX_HP
        it.jmp = MAX_JMP
        it.jmping = False
        it.boost = MAX_BOOST
        it.angle = 0
        it.offset = Vector(0,0)
        it.no_dmg_time=0
    def update(it):
        it.pos += it.vel
        it.vel.y += 3
        if it.pos.y > GROUND:
            it.on_ground=True
            it.jmp = MAX_JMP
            it.pos.y=GROUND
            it.vel.y=0
        else:
            it.on_ground=False
        pressed_keys = pygame.key.get_pressed()
        just_pressed_keys = pygame.key.get_just_pressed()
        just_released_keys = pygame.key.get_just_released()
        if just_pressed_keys[pygame.K_SPACE] and it.jmp > 0:
            it.jmp-=1
            it.boost=MAX_BOOST
            it.jmping=True
        if just_released_keys[pygame.K_SPACE]:
            it.jmping=False
        if it.jmping and it.boost > 0:
            it.boost-=1
            it.vel.y=-20
        if pressed_keys[pygame.K_RSHIFT]:
            it.state = State.SLIDE
        else:
            it.state = State.STAND
        if not it.on_ground and it.jmp == 0:
            it.angle-=20
        else :
            it.angle=0
    def check_collide(it,x2,y2,w2,h2):
        size=PLR_SIZE_BY_STATE[it.state]
        offset=PLR_OFFSET_BY_STATE[it.state]
        x1,y1=it.pos+offset
        w1,h1=size

        return (
            x1-w1*0.5 < x2+w2*0.5 and
            x2-w2*0.5 < x1+w1*0.5 and
            y1-h1*0.5 < y2+h2*0.5 and
            y2-h2*0.5 < y1+h1*0.5
        )
    def draw(it,screen):
        size=PLR_SIZE_BY_STATE[it.state]
        offset=PLR_OFFSET_BY_STATE[it.state]
        alpha = 255 if it.no_dmg_time%10<5 else 100
        draw_rect(screen, *(it.pos+offset), *size, (0,0,0,alpha), it.angle)

gameState=None
def init(gs):
    global gameState
    gameState=gs
    gameState.initial_plr = Player()
    return

def do(screen):
    if not gameState:
        return
    for event in ev.poll(ev.PLR_DMG):
        if gameState.plr.no_dmg_time > 0:
            continue
        gameState.plr.hp-=1
        gameState.plr.no_dmg_time=60
    if gameState.plr.no_dmg_time > 0:
        gameState.plr.no_dmg_time-=1
    if gameState.plr.hp < 1:
        gameState.state=0
    gameState.plr.update()
    gameState.plr.draw(screen)
    hp=gameState.plr.hp
    text_surf = gameState.font.render("■"*hp+"□"*min(MAX_HP-hp,3), True, (255, 0, 0))
    screen.blit(text_surf, (50, 50))
    return
