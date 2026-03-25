import pygame as pg
from random import randrange as rr
from baloon import Balloon, DATA

pg.init()
size = (600, 400)
screen = pg.display.set_mode(size)
pg.display.set_caption('OSU)')
icon = pg.surface.Surface((100, 100), pg.SRCALPHA)
pg.draw.ellipse(icon, (0, 0, 0), (0, 0, 100, 100))
pg.draw.ellipse(icon, (255, 0, 0), (40, 40, 20, 20))
pg.display.set_icon(icon)

run = True
bls = pg.sprite.Group()
clock = pg.time.Clock()
speed = 20
fnt = pg.font.Font(None, 40)
cdfnt = pg.font.Font(None, 400)
chance = 2000
countdown = 10000
last = [0]
nm = 0

success = 0.0  # накопленный успех (0.1)

while run:
    tick = clock.tick()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
        if i.type == pg.MOUSEBUTTONDOWN:
            click_flag = [False]
            bls.update(0, speed, i.pos, last, click_flag)
            if click_flag[0]:
                
                success = min(success + 0.01, 1.0)

    screen.fill((100, 100, 255))

    # Спавн шариков
    if rr(int(chance)) == 0:
        x = rr(size[0] - 50)
        Balloon(bls, size, x, nm)
        nm += 1

    # Обновление 
    bls.update(tick, speed)
    bls.draw(screen)

    # Динамика сложности
    if speed >= 10:
        speed -= tick / 2000
    if chance > 500:
        chance -= tick / 30
    else:
        countdown -= tick
        cd = cdfnt.render(str(countdown // 1000), True, (255, 0, 255))
        screen.blit(cd, (0, 50))

    
    acc_display = int(success * 10000) / 100
    score = fnt.render(f'ACCURACY: {acc_display} % ', True, (0, 0, 0))
    screen.blit(score, (0, 0))

    pg.display.flip()

    if countdown <= 1:
        run = False

# Финальный экран
run = True
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False
    screen.fill((100, 100, 255))
    final_acc = int(success * 10000) / 100
    score = fnt.render(f'ACCURACY: {final_acc} % ', True, (0, 0, 0))
    screen.blit(score, (0, 200))
    pg.display.flip()
