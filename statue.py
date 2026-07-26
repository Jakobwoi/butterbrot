import pygame

class Statue():
    def __init__(self, window, pos, faces, face):
        self.window = window
        self.pos = pos
        self.faces = faces
        self.face = face
        self.canSwap = True
    
    def draw(self):
        self.window.blit(self.faces[f"Statue_{self.face}"], self.pos)
    
    def checkCollision(self, playerPos, playerSize):
        statueRect = pygame.Rect(self.pos, self.faces[f"Statue_{self.face}"].get_size())
        playerRect = pygame.Rect(playerPos, playerSize)
        # playerRect = pygame.Rect((50, 100), (100, 200))
        pygame.draw.rect(self.window, "red", statueRect, 3)
        pygame.draw.rect(self.window, "green", playerRect, 3)
        return statueRect.colliderect(playerRect)
    
    def swap(self, newFace):
        oldFace = self.face
        self.face = newFace
        return oldFace