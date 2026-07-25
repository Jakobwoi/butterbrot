import pygame
from player import Player
import os

pygame.init()
screen = pygame.display.set_mode((600, 600))
faces = dict()
for path in os.listdir("images/"):
    faces[path.removesuffix(".png")] = pygame.image.load(f"images/{path}")

player = Player(screen, pygame.Vector2(50, 50), "Invisibility", faces)
clock = pygame.time.Clock()


running = True
while running:
    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d])

    screen.fill("grey")
    player.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(60)

pygame.quit()