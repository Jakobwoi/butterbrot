import pygame
from player import Player
import os
from statue import Statue

pygame.init()
screen = pygame.display.set_mode((600, 600))
statueImage = pygame.image.load("assets/statue_after_switching.png")
faces = dict()
for path in os.listdir("images/"):
    faces[path.removesuffix(".png")] = pygame.image.load(f"images/{path}")

player = Player(screen, pygame.Vector2(50, 50), "Normal", faces)
statue = Statue(screen, pygame.Vector2(500, 70), statueImage, "Invisibility")
clock = pygame.time.Clock()

running = True
while running:
    keys = pygame.key.get_pressed()
    player.move(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d])

    screen.fill("grey")
    statue.draw()
    player.draw()
    pygame.display.flip()

    print(statue.checkCollision(player.pos, faces["".join([str(x) for x in player.faceImage])].get_size()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    clock.tick(60)

pygame.quit()