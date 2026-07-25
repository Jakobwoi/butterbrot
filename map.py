import pygame
import essentials as es

screen = None
class camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
cam = camera(0,0)

class tile:
    def __init__(self, name, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sizey = sy
        self.sizex = sx
        self.tex = es.load_sprite(name)
        self.lscale = 1

def init():
    global map
    map = [[],[]]

def load_map(name):
    global map
    map = maps.get(name, [[],[]])


maps = {
    "test": [
        [tile("test", 0, 0, 32, 32), tile("test", 32, 0, 32, 32)],
        [tile("test", 0, 32, 32, 32), tile("test", 32, 32, 32, 32)]
    ]
}



def draw():
    surface = pygame.display.get_surface()
    if surface is None:
        return

    midx = surface.get_width() / 2
    midy = surface.get_height() / 2
    for x in map:
        for y in x:
            y.out = y.tex
            y.out2 = pygame.transform.scale(y.out, (y.sizex*y.lscale,y.sizey*y.lscale))
            y.out_rect = y.out2.get_rect(center=(midx+y.x+cam.x, midy+y.y+cam.y))
            surface.blit(y.out2, y.out_rect)