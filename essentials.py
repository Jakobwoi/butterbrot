from pathlib import Path
import pygame

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.joinpath("assets")

def load_sprite(name):
    path = ASSETS_DIR.glob("**/" + name + "*")
    return pygame.image.load(list(path)[0])