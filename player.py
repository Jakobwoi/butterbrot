import pygame
import essentials

class Player():
    def __init__(self, window, position, face, body):
        self.window = window
        self.position = position
        self.face = face
        self.body = body

    def draw(self):
        pass

    def move(self, w, a, s, d):
        pass

    def change_face(self, face):
        self.face = face