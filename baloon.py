import pygame as pg

DATA = [0, 0]  # DATA[0] – всего шариков (удалённых кликом или улетевших),
               # DATA[1] – пропущенных (улетевших)

class Balloon(pg.sprite.Sprite):
    image = pg.surface.Surface((50, 50), pg.SRCALPHA)
    pg.draw.ellipse(image, (255, 0, 0), (0, 0, 50, 50))

    def __init__(self, group, size, x, num):
        super().__init__(group)
        self.image = Balloon.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, size[1]
        self.dy = 0
        self.size = self.rect.size[0]
        self.group = group
        self.num = num

    def update(self, tick, speed, pos=None, click_flag=None):
        """
        tick – время с прошлого кадра (мс)
        speed – скорость подъёма
        pos – позиция клика (если указана)
        click_flag – список для сигнала, что был клик по этому шарику
        """
        # Обработка клика
        if pos is not None:
            if (pos[0] - self.size <= self.rect.x <= pos[0] and
                pos[1] - self.size <= self.rect.y <= pos[1]):
                self.remove(self.group)
                if click_flag is not None:
                    click_flag[0] = True  # сообщаем, что клик произошёл
                # НЕ увеличиваем DATA[0] при клике
                return

        # Обычное движение
        self.dy += tick / speed
        if self.dy > 1:
            self.rect.y -= int(self.dy)
            self.dy -= int(self.dy)

        # Проверка выхода за верхнюю границу
        if self.rect.y <= -1 * self.size:
            self.remove(self.group)
            DATA[0] += 1
            DATA[1] += 1
