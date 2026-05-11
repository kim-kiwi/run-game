import pygame

width,height=0,0
b1=[0,0]
b2=[0,0]

def init(w,h):
    global width,height,b1,b2
    width, height = w, h
    b1=[0,0]
    b2=[width,0]
    return


def do(screen):
    b1[0]-=1
    b2[0]-=1
    if b1[0] < -width:
        b1[0]=width
    if b2[0] < -width:
        b2[0]=width
    pygame.draw.rect(screen, (255,0,0), (*b1,width,height))
    pygame.draw.rect(screen, (0,255,0), (*b2,width,height))
    return
