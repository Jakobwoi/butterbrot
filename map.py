import pygame
import essentials as es
screen = pygame.display.get_surface()

def __init__():
    init()

def init():
    global map
    map = [[],[]]

class tile:
    def __init__(self,name,x,y,sx,sy):
        self.x = x
        self.y = y
        self.sizey = sy
        self.sizex = sx
        self.tex = es.load_sprite(name)

test = tile("test",0,0,32,32)

def draw():
    midx = pygame.display.get_surface().get_width() / 2
    midy = pygame.display.get_surface().get_height() / 2
    for x in map:
        for y in x:
            y.out = self.tex
            y.out2 = pygame.transform.scale(y.out, (y.sizex*y.lscale,y.sizey*y.lscale))
            y.out_rect = y.out2.get_rect(center=(midx+y.x, midy+y.y))
            screen.blit(y.out2, y.out_rect)