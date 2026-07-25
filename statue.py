import pygame

class Statue():
    def __init__(self, window, pos, image, face):
        self.window = window
        self.pos = pos
        self.image = image
        self.face = face
    
    def draw(self):
        self.window.blit(self.image, self.pos)
    
    def checkCollision(self, playerPos, playerSize):
        statueRect = pygame.Rect(self.pos, self.image.get_size())
        playerRect = pygame.Rect(playerPos, playerSize)
        return statueRect.colliderect(playerRect)
    
    def swap(self, newFace):
        oldFace = self.face
        self.face = newFace
        return oldFace