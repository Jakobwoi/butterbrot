import pygame
import random
import essentials as es

enemy_types = {"enemy0": 10, "enemy1": 11, "enemy2": 12}

def init():
    global enemys
    enemys = dict()

class enemy:
    def __init__(self, window, pos, health, type, id):
        self.window = window
        self.pos = pos
        self.health = health
        self.type = type
        self.id = id
    def update(self):
        pass
    def draw(self):
        sprite = es.load_sprite(self.type)
        self.window.blit(sprite, self.pos)

def spawn(window, pos, health, type):
    global enemys
    enemy_id = int(str(enemy_types[type]) + ("{:02d}".format(random.randint(0, 99)))) # player id is 4 digits, first 2 digits are type, last 2 are random
    print("Spawning enemy with id: " + str(enemy_id))
    tempenemy = enemy(window, pos, health, type, enemy_id)
    enemys[enemy_id] = tempenemy

def delete(id):
    global enemys
    if id in enemys:
        del enemys[id]