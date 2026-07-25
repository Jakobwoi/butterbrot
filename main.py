import pygame
import asyncio
import os

import map
import enemys
import essentials as es

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
pygame.display.set_caption("Butterbrot")
clock = pygame.time.Clock()

from player import Player
faces = dict()
for path in os.listdir("images/"):
    faces[path.removesuffix(".png")] = pygame.image.load(f"images/{path}")
player = Player(screen, pygame.Vector2(0, 0),"Invisibility", faces)

map.init()
map.load_map("test")
level = 1
l1music = es.load_music("oberweltidk")
l1playing = Falseenemys.init()

running = True
enemys.spawn(screen, (100, 100), 100, 5, 2, "Face1")
async def main():
    global running,screen,player
    while running:
        if level == 1 and not l1playing:
            l1music.play(-1)
            
        elif level != 1 and l1playing:
            l1music.stop()
            


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
        if pygame.key.get_pressed()[pygame.K_a] == True:
            map.cam.x += 2.828
        if pygame.key.get_pressed()[pygame.K_d] == True:
            map.cam.x -= 2.828
        if pygame.key.get_pressed()[pygame.K_w] == True:
            map.cam.y += 2.828
        if pygame.key.get_pressed()[pygame.K_s] == True:
            map.cam.y -= 2.828
        if pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
            print("Escape key pressed")   

        if level == 1:
            pass


        keys = pygame.key.get_pressed()
        player.move(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d]) 

        screen.fill("blue")
        map.draw()
        player.draw()
        for enemy in enemys.enemys.values():
            enemy.update()
            enemy.draw()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())