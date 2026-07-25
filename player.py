import pygame
from math import sqrt
import map

class Player():
    def __init__(self, window, pos, face, faces):
        self.window = window
        self.pos = pos
        self.face = face
        self.faces = faces
        self.health = 100
        self.speed = 2
        self.strength = 5
        self.lscale = 1
        self.visible = True
        self.telePoint = pos
        self.faceImage = list("Face0_0010_0")
        self.walkCount = 0


    def draw(self):
        surface = pygame.display.get_surface()
        if surface is None:
            return
        midx = surface.get_width() / 2
        midy = surface.get_height() / 2
        print("Drawing player at position: ", (self.pos[0]+midx, self.pos[1]+midy))
        out = self.faces["".join([str(x) for x in self.faceImage])]
        out2 = pygame.transform.scale(out, (out.get_width()*self.lscale,out.get_height()*self.lscale))
        out_rect = out2.get_rect(center=(midx+self.pos[0]+map.cam.x, midy+self.pos[1]+map.cam.y))
        surface.blit(out2, out_rect)

    def move(self, w, a, s, d):
        horizontalMove = d - a
        verticalMove = w - s
        if not (abs(horizontalMove) == 1 and abs(verticalMove) == 1):
            self.pos = (self.pos[0] + horizontalMove * sqrt(2) * self.speed, self.pos[1] - verticalMove * sqrt(2) * self.speed)
        else:
            self.pos = (self.pos[0] + horizontalMove * self.speed, self.pos[1] - verticalMove * self.speed)
        if horizontalMove == 0 and verticalMove == 0:
            self.walkCount = 0
        elif not (abs(horizontalMove) == 1 and abs(verticalMove) == 1): 
            self.faceImage[6] = int(verticalMove == 1)
            self.faceImage[7] = int(horizontalMove == -1)
            self.faceImage[8] = int(verticalMove == -1)
            self.faceImage[9] = int(horizontalMove == 1)
            self.walkCount += 1
        else:
            self.faceImage[6] = 0
            self.faceImage[7] = int(horizontalMove == -1)
            self.faceImage[8] = 0
            self.faceImage[9] = int(horizontalMove == 1)
            self.walkCount += 1
        self.faceImage[11] = (self.walkCount * self.speed // 15) % 4

    def swap(self, newFace):
        oldFace = self.face
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
            print(oldFace)
        return oldFace
    
    def setTelePoint(self, pos):
        if self.face == "Teleportation":
            self.telePoint = self.pos

    def teleport(self):
        if self.face == "Teleportation":
            self.pos, self.telePoint = self.telePoint, self.pos
