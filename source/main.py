import pygame as pg


HEIGHT = WIDTH = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}

def loadImages():
    pieces = ['wR,', 'wN', 'wB', 'wQ', 'wK', 'wP', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bP']
    for piece in pieces:
        IMAGES[piece] = pg.image.load("../images/" + piece + ".png")
    
    


