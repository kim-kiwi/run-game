import pygame
import random
from utils import Vector, draw_rect, GameState
import ev

gameState=None

spikes=[]

class Spike:
    def __init__(it,x,y):
        it.pos=Vector(x,y)
        it.blink=0
    def update(it):
        it.pos.x-=gameState.speed
        if it.pos.x < -gameState.width:
            return False
        if gameState.plr.check_collide(*it.pos,50,50):
            ev.emit(ev.PLR_DMG)

        return True
    def draw(it,screen):
        it.blink+=1
        c=(255,0,0) if it.blink%20<10 else (0,255,255)
        draw_rect(screen, *it.pos, 50, 50, c)

def init(gs: GameState):
    global gameState,spikes
    spikes=[]
    gameState=gs
    return

tick=0
def do(screen):
    global tick
    if not gameState:
        return
    if tick>600:
        tick=0
        spikes.append(Spike(1400,random.randint(50,950)))
    tick+=1*gameState.speed
    del_spikes=[]
    for i,spike in enumerate(spikes):
        alive=spike.update()
        if not alive:
            del_spikes.append(i)
        spike.draw(screen)
    for i in del_spikes:
        spikes.pop(i)
    return
