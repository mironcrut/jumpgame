import pygame as pg
from config import *

pg.init()

display = pg.display.set_mode(DISPLAY)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    display.fill("black")
    pg.display.update()

    clock.tick(FPS)