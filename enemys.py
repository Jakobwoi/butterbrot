import pygame
import random

enemy_types = {"enemy0": 10, "enemy1": 11, "enemy2": 12}

def init():
    global enemys
    enemys = dict()

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
    enemy_id = int(str(enemy_types[type]) + ("{:02d}".format(random.randint(0, 99)))) # player id is 4 digits, first 2 digits are type, last 2 are random
    print("Spawning enemy with id: " + str(enemy_id))
    tempenemy = enemy(x,y,type, enemy_id)
    enemys[enemy_id] = tempenemy

def delete(id):
    global enemys
    if id in enemys:
        del enemys[id]