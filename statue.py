import pygame

class Statue():
    def __init__(self, window, pos, image, face):
        self.window
        self.pos = pos
        self.image = image
        self.face = face
    
    def draw(self):
        self.window.blit(self.image, self.pos)
    
    def checkCollision(self, playerPos):
        statueRect = pygame.Rect(self.pos, self.image.get_size())