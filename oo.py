from pygame import *

class GameSprite(sprite.Sprite):
    # картинка, x, y, ширина, высота, скорость
    def __init__(self, picture, xcoord, ycoord, width, height, speed):
        super().__init__() # установка начальных свойств игрового обЪекта pygame
        self.image = transform.scale(image.load(picture), (width, height))
        self.rect = self.image.get_rect() # хитбокс(область столкновений)
        self.rect.x = xcoord
        self.rect.y = ycoord
        self.speed = speed

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((800, 600))
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'), (800, 600))

hero = GameSprite('sprite2.png', 200, 200, 80, 80, 10)

game = True
while game:
    window.blit(background, (0,0))
    for ev in event.get():
        if ev.type == QUIT:
            game = False

    hero.show()
    display.update()
    time.delay(50)