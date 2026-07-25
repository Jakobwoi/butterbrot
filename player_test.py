import pygame
from player import Player

pygame.init()
face1 = pygame.image.load("images/face1.jpg")
screen = pygame.display.set_mode((320, 320))
player = Player(screen, pygame.Vector2(50, 50), "Invisibility", "standard")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill("grey")
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()