import pygame
import random

def init():
    global enemys
    enemys = []

class enemy:
    def __init__(self,x,y,type, id):
        self.x = x
        self.y = y
        self.type = type
        self.id = id
    def update():
        pass
    def draw():
        pass

def spawn(x,y,type):
    global enemys
    tempenemy = enemy(x,y,type)
    enemys.append(tempenemy)

def delete(id):
    global enemys
    for en in enemys:
        if en.id == id:
            enemys.remove(en)
