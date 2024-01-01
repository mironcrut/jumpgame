import pygame as pg
from config import *

pg.init()

display = pg.display.set_mode(DISPLAY)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

    display.fill("black")
    if player.is_alive:
        player.update()
        spike.update()

    pg.display.update()

    clock.tick(FPS)