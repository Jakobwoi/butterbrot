import pygame
import essentials as es

screen = None
class camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
cam = camera(0,0)

class tile:
    def __init__(self, name, x, y, sx, sy, lscale, is_exit=False):
        self.x = x
        self.y = y
        self.sizey = sy
        self.sizex = sx
        self.tex = es.load_sprite(name)
        self.lscale = lscale
        self.is_exit = is_exit

def init():
    global map
    map = [[],[]]

def load_map(name):
    global map
    map = maps.get(name, [[],[]])

maps = {
    "level1": [[]]
    # "test": [
    #     [tile("test", 0, 0, 32, 32,1), tile("test", 32, 0, 32, 32,1)],
    #     [tile("test", 0, 32, 32, 32,1), tile("test", 32, 32, 32, 32,1)]
    # ],

    # "level1": [
    #     # Row 0 (top)
    #     [tile("grass_upper_left_tile", 0, 0, 32*8, 32*8, 4), 
    #      tile("grass_upper_tile", 256*4, 0, 32*8, 32*8, 4), 
    #      tile("grass_upper_right_tile", 256*8, 0, 32*8, 32*8, 4)],
    #     # Row 1 (middle)
    #     [tile("grass_left_tile", 0, 256*4, 32*8, 32*8, 4), 
    #      tile("test", 256*4, 256*4, 32*8, 32*8, 4, is_exit=True), 
    #      tile("grass_right_tile", 256*8, 256*4, 32*8, 32*8, 4)],
    #     # Row 2 (bottom)
    #     [tile("grass_lower_left_tile", 0, 256*8, 32*8, 32*8, 4), 
    #      tile("grass_lower_tile", 256*4, 256*8, 32*8, 32*8, 4), 
    #      tile("grass_lower_right_tile", 256*8, 256*8, 32*8, 32*8, 4)]
    # ]
}



def draw():
    surface = pygame.display.get_surface()
    if surface is None:
        return

    midx = surface.get_width() / 2
    midy = surface.get_height() / 2
    for x in map:
        for y in x:
            y.out = y.tex
            y.out2 = pygame.transform.scale(y.out, (y.sizex*y.lscale,y.sizey*y.lscale))
            y.out_rect = y.out2.get_rect(center=(midx+y.x+cam.x, midy+y.y+cam.y))
            surface.blit(y.out2, y.out_rect)

def check_exit(player_pos):
    """Prüft, ob der Spieler auf dem Ausgang (middle Tile) ist"""
    for row in map:
        for tile_obj in row:
            if tile_obj.is_exit:
                # Exit Mittelpunkt
                exit_center_x = tile_obj.x + (tile_obj.sizex * tile_obj.lscale) / 2
                exit_center_y = tile_obj.y + (tile_obj.sizey * tile_obj.lscale) / 2
                
                # Distance berechnen
                distance = ((player_pos[0] - exit_center_x)**2 + (player_pos[1] - exit_center_y)**2)**0.5
                
                # Debug-Info
                print(f"Player: {player_pos}, Exit: ({exit_center_x}, {exit_center_y}), Distance: {distance}")
                
                # Größerer Radius (halbe Tile-Größe = ~200px)
                if distance < 200:
                    print("✓ Exit erreicht!")
                    return True
    return False