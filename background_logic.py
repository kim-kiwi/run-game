import pygame
import random

gameState=None
bgs=[]

class Background:
    def __init__(self,pos,color):
        self.pos = pos
        self.color = color
    def update(self):
        self.pos[0]-=gameState.speed
        if self.pos[0] < -gameState.width:
            bgs.append(Background([self.pos[0]+gameState.width*2,0],[random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
            return False
        return True
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.pos,gameState.width,gameState.height))

def init(gs):
    global gameState,bgs
    gameState=gs
    bgs=[]
    bgs.append(Background([0,0],[random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
    bgs.append(Background([gameState.width,0],[random.randint(0,255),random.randint(0,255),random.randint(0,255)]))
    return


def do(screen):
    if not gameState:
        return
    del_bg=[]
    for i,bg in enumerate(bgs):
        if not bg.update():
            del_bg.append(i)
        bg.draw(screen)
    for del_bg_i in del_bg:
        bgs.pop(del_bg_i)
    return
