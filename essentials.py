from pathlib import Path
import pygame

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.joinpath("assets")
MUSIC_DIR = BASE_DIR.joinpath("music")

def load_sprite(name):
    path = ASSETS_DIR.glob("**/" + name + "*")
    return pygame.image.load(list(path)[0])

def load_music(name):
    path = MUSIC_DIR.glob("**/" + name + "*")
    return pygame.mixer.Sound(list(path)[0])