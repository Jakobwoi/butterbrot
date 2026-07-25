import pygame
from math import sqrt

class Player():
    def __init__(self, window, pos, face, faces):
        self.window = window
        self.pos = pos
        self.face = face
        self.faces = faces
        self.health = 100
        self.speed = 2
        self.strength = 5
        self.visible = True
        self.telePoint = pos
        self.faceImage = "Face0_0010_0"
        self.walkCount = 0

    def update():
        pass

    def draw(self):
        self.window.blit(self.faces[self.faceImage], self.pos)

    def move(self, w, a, s, d):
        horizontalMove = d - a
        verticalMove = w - s
        if not (abs(horizontalMove) == 1 and abs(verticalMove) == 1):
            self.pos = (self.pos[0] + horizontalMove * sqrt(2) * self.speed, self.pos[1] - verticalMove * sqrt(2) * self.speed)
        else:
            self.pos = (self.pos[0] + horizontalMove * self.speed, self.pos[1] - verticalMove * self.speed)
        if horizontalMove == 0 and verticalMove == 0:
            self.walkCount = 0
        else: 
            self.faceImage[6] = horizontalMove == 1
            self.faceImage[7] = verticalMove == -1
            self.faceImage[8] = horizontalMove == -1
            self.faceImage[9] = verticalMove == 1
            self.walkCount += 1
        self.walkCount += 1
        self.faceImage[11] = self.walkCount % 4

    def swap(self, newFace):
        oldFace = newFace
        self.face = newFace
        self.faceImage[4] = ["Normal", "Invisibility", "Teleportation", "Super Speed", "Super Strength"].index(newFace)
        if newFace == "Normal":
            self.speed = 2
            self.visible = True
            self.strength = 5
        if newFace == "Invisibility":
            self.speed = 2
            self.visible = False
            self.strength = 5
        if newFace == "Teleportation":
            self.speed = 2
            self.visible = True
            self.strength = 5
            self.telePoint = self.pos
        if newFace == "Super Speed":
            self.speed = 5
            self.visible = True
            self.strength = 5
        if newFace == "Super Strength":
            self.speed = 2
            self.visible = True
            self.strength = 20
        return oldFace
    
    def setTelePoint(self, pos):
        if self.face == "Teleportation":
            self.telePoint = self.pos

    def teleport(self):
        if self.face == "Teleportation":
            self.pos, self.telePoint = self.telePoint, self.pos