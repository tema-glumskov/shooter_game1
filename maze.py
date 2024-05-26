from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, xcoord, ycoord, width, height, speed, picture):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(picture), (width, height))  
        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord
        self.speed = speed

    def hero_update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

    def enemy_update(self):
        self.rect.x -= self.speed
        if self.rect.x < 400:
            self.speed *= -1
        if self.rect.x > 650:
            self.speed *= -1

    def enemy_update2(self):
        self.rect.y -= self.speed
        if self.rect.y < 300:
            self.speed *= -1
        if self.rect.y > 450:
            self.speed *= -1

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background2.png'), (700, 500))

hero = GameSprite(10, 10, 60, 60, 12, 'hero.png')
enemy = GameSprite(610, 350, 60, 60, 10, 'cyborg.png')
enemy2 = GameSprite(515, 410, 60, 60, 10, 'cyborg.png')
target = GameSprite(600, 400, 90, 90, 10, 'treasure.png')
wall = GameSprite(100, 90, 150, 40, 10, 'stena1.jpg')
wall2 = GameSprite(180, 200, 40, 280, 10, 'stena1.jpg')
wall3 = GameSprite(210, 200, 168, 50, 10, 'stena1.jpg')
wall4 = GameSprite(70, 90, 40, 150, 10, 'stena1.jpg')
wall5 = GameSprite(70, 190, 40, 150, 10, 'stena1.jpg')
wall6 = GameSprite(250, 90, 195, 40, 10, 'stena1.jpg')
wall7 = GameSprite(445, 50, 40, 260, 10, 'stena1.jpg')
wall8 = GameSprite(340, 230, 40, 150, 10, 'stena1.jpg')
wall9 = GameSprite(277, 340, 90, 45, 10, 'stena1.jpg')

walls = sprite.Group() # группа стен
walls.add(wall)
walls.add(wall2)
walls.add(wall3)
walls.add(wall4)
walls.add(wall5)
walls.add(wall6)
walls.add(wall7)
walls.add(wall8)
walls.add(wall9)

font.init()
font1 = font.Font(None, 48)
text = font1.render('Ура! Ты дошел до домика!', True, (36, 250, 109))

game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.spritecollide(hero, walls, False):
        hero.rect.x = 10
        hero.rect.y = 10

    if sprite.collide_rect(hero, enemy):
        hero.rect.x = 10
        hero.rect.y = 10

    if sprite.collide_rect(hero, enemy2):
        hero.rect.x = 10
        hero.rect.y = 10

    if sprite.collide_rect(hero, target):
        window.blit(text, (100,200))
    
    hero.hero_update()
    enemy.enemy_update()
    enemy2.enemy_update2()
    hero.reset()
    enemy.reset()
    walls.draw(window)
    enemy2.reset()
    target.reset()
    display.update()
    time.delay(50)