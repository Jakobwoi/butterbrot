import pygame
import random
import essentials as es
from math import sqrt
import map

enemy_types = {"enemy0": 10, "enemy0-i": 20, "enemy2": 12, "Face1": 13}

def init():
    global enemys
    enemys = dict()

class enemy:
    def __init__(self, window, pos, health, strength, speed, type, id):
        self.window = window
        self.pos = pos
        self.health = health
        self.strength = strength
        self.speed = speed
        self.type = type
        self.id = id
        self.current = list(type + "_0010_0")
        self.sprites = dict()
        # dirs = list("0000")
        # for i in range(0, 4, 2):
        #     dirs[i] = "1"
        #     for l in range(1, 4, 2):
        #         for t in range(2):
        #             dirs[l] = str(t)
        #             for j in range(4):
        #                 print("Loaded sprite: " + type + "_"+ ''.join(dirs) +"_" + str(j))
        #                 self.sprites[type + "_"+ ''.join(dirs) +"_" + str(j)] = es.load_sprite(type + "_" + ''.join(dirs) + "_" + str(j))
        #             dirs[l] = "0"
        #     dirs[i] = "0"
        dirs = list("0001")
        for j in range(4):
            print("Loaded sprite: " + type + "_"+ ''.join(dirs) +"_" + str(j))
            self.sprites[type + "_"+ ''.join(dirs) +"_" + str(j)] = es.load_sprite(type + "_" + ''.join(dirs) + "_" + str(j))
            # dirs[i+2] = "0"
        dirs = list("0100")
        for j in range(4):
            print("Loaded sprite: " + type + "_"+ ''.join(dirs) +"_" + str(j))
            self.sprites[type + "_"+ ''.join(dirs) +"_" + str(j)] = es.load_sprite(type + "_" + ''.join(dirs) + "_" + str(j))
            # dirs[i+2] = "0"

        self.walkCount = 0
        self.loopCount = 0
        self.loopLength = 100
    
        self.moveX = 0
        self.moveY = 1
    
    def update(self):
        if self.loopCount < self.loopLength:
            self.loopCount += 1
        else:
            self.loopCount = 0
            self.moveY = self.moveY * -1
        self.move(self.moveX, self.moveY)
        self.draw()

    def move(self, x, y):
        if not (abs(x) == 1 and abs(y) == 1):
            self.pos = (self.pos[0] + x * sqrt(2)/2 * self.speed, self.pos[1] - y * sqrt(2)/2 * self.speed)
        else:
            self.pos = (self.pos[0] + x * self.speed, self.pos[1] - y * self.speed)
        if x == 0 and y == 0:
            self.walkCount = 0
        else: 
            self.current[len(self.type)+1] = int(y == 1)
            self.current[len(self.type)+2] = int(x == -1)
            self.current[len(self.type)+3] = int(y == -1)
            self.current[len(self.type)+4] = int(x == 1)
            print("".join([str(x) for x in self.current]))
            self.walkCount += 1
        self.current[len(self.type)+6] = (self.walkCount * self.speed // 5) % 4

    def draw(self):
        sprite = self.sprites["".join([str(x) for x in self.current])]
        self.window.blit(sprite, (self.pos[0] + map.cam.x, self.pos[1] + map.cam.y))

def spawn(window, pos, health, strength, speed, type):
    global enemys
    enemy_id = int(str(enemy_types[type]) + ("{:02d}".format(random.randint(0, 99)))) # player id is 4 digits, first 2 digits are type, last 2 are random
    print("Spawning enemy with id: " + str(enemy_id))
    tempenemy = enemy(window, pos, health, strength, speed, type, enemy_id)
    enemys[enemy_id] = tempenemy

def delete(id):
    global enemys
    if id in enemys:
        del enemys[id]