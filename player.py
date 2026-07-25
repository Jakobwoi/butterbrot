import pygame
from math import sqrt

class Player():
    def __init__(self, window, pos, face, face1, face2, face3, face4):
        self.window = window
        self.pos = pos
        self.face = face
        self.face1 = face1
        self.face2 = face2
        self.face3 = face3
        self.face4 = face4
        self.health = 100
        self.speed = 2
        self.visible = True
        self.telePoint = pos


    def draw(self):
        if self.face == "Invisibility":
            self.window.blit(self.face1, self.pos)

    def move(self, w, a, s, d):
        horizontalMove = d - a
        verticalMove = w - s
        if not (abs(horizontalMove) == 1 and abs(verticalMove) == 1):
            self.pos = (self.pos[0] + horizontalMove * sqrt(2) * self.speed, self.pos[1] - verticalMove * sqrt(2) * self.speed)
        else:
            self.pos = (self.pos[0] + horizontalMove * self.speed, self.pos[1] - verticalMove * self.speed)

