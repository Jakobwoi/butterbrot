import pygame
import asyncio

import map

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
pygame.display.set_caption("Butterbrot")
clock = pygame.time.Clock()
map.init()
map.load_map("test")


running = True
async def main():
    global running,screen
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
            if pygame.key.get_pressed()[pygame.K_a] == True:
                map.cam.x += 10
            elif pygame.key.get_pressed()[pygame.K_d] == True:
                map.cam.x -= 10
            elif pygame.key.get_pressed()[pygame.K_w] == True:
                map.cam.y += 10
            elif pygame.key.get_pressed()[pygame.K_s] == True:
                map.cam.y -= 10
            elif pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                print("Escape key pressed")    

        screen.fill("blue")
        map.draw()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())