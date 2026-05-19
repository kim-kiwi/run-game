import pygame

class Vector:
    def __init__(it,x,y):
        it.x=x
        it.y=y
    def __iter__(it):
        return iter([it.x,it.y])
    def __add__(it,other):
        if isinstance(other,Vector):
            return Vector(it.x+other.x,it.y+other.y)
        elif isinstance(other,(int,float)):
            return Vector(it.x+other,it.y+other)
    def __sub__(it, other):
        if isinstance(other,Vector):
            return Vector(it.x-other.x,it.y-other.y)
        elif isinstance(other,(int,float)):
            return Vector(it.x-other,it.y-other)
    def __mul__(it, other):
        if isinstance(other,(int,float)):
            return Vector(it.x*other,it.y*other)

def draw_rect(screen,x,y,w,h,c,r=0,width=0):
    rect_surf = pygame.Surface((w,h), pygame.SRCALPHA)
    pygame.draw.rect(rect_surf, c, (0,0,w,h), width=width)
    rotated_rect_surf = pygame.transform.rotate(rect_surf, r)
    rect = rotated_rect_surf.get_rect(center=(x,y))
    screen.blit(rotated_rect_surf, rect.topleft)

class GameState:
    def __init__(it,state,speed,font,width,height,plr):
        it.initial_state=state
        it.initial_speed=speed
        it.initial_font=font
        it.initial_width=width
        it.initial_height=height
        it.initial_plr=plr 
        it.reset()
    def reset(it):
        it.state=it.initial_state
        it.speed=it.initial_speed
        it.font=it.initial_font
        it.width=it.initial_width
        it.height=it.initial_height
        it.plr=it.initial_plr 

