import pygame as pg


DATA = [0, 0]


class Balloon(pg.sprite.Sprite):
    image = pg.surface.Surface((50, 50), pg.SRCALPHA)
    pg.draw.ellipse(image, (255, 0, 0), (0, 0, 50, 50))

    def __init__(self, group, size, x, num):
        global DATA
        super().__init__(group)
        self.image = Balloon.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, size[1]
        self.dy = 0
        self.size = self.rect.size[0]
        self.group = group
        self.num = num

    def update(self, tick, speed, pos=None, sc=None):
        global DATA
        if not pos is None:
            if pos[0] - self.size <= self.rect.x <= pos[0] and pos[1] - self.size <= self.rect.y <= pos[1]:
                self.remove(self.group)
                DATA[0] += 1
        if not sc is None:
            sc[0] = self.num
        self.dy += tick / speed
        if self.dy > 1:
            self.rect.y -= int(self.dy)
            self.dy -= int(self.dy)
        if self.rect.y <= -1 * self.size:
            self.remove(self.group)
            DATA[0] += 1
            DATA[1] += 1