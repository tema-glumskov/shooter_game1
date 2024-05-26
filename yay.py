# подключение нужных модулей
from pygame import *
from random import randint 
from time import time as timer

# класс игрового объекта
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, xcoord, ycoord, width, height, speed, picture):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(picture), (width, height))  
        self.rect = self.image.get_rect()
        self.rect.x = xcoord
        self.rect.y = ycoord
        self.speed = speed

    # метод перемещения игрока с клавиатуры
    def rocket_update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

    # метод перемещения пули
    def bullet_update(self):
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()
    
    # методы перемещения врагов
    def enemy_update(self):
        self.rect.y += self.speed

    def enemy_update2(self):
        self.rect.y += self.speed

    def enemy_update3(self):
        self.rect.y += self.speed

    def enemy_update4(self):
        self.rect.y += self.speed

    def enemy_update5(self):
        self.rect.y += self.speed

    def enemy_update6(self):
        self.rect.y += self.speed

    def enemy_update7(self):
        self.rect.y += self.speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# настройка игрового окна
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('background3.png'), (700, 500))

# создание игровых объектов
rocket = GameSprite(285, 300, 50, 150, 14, 'rocket.png')
enemy = GameSprite(99, 100, 60, 70, 12, 'alien.png')
enemy2 = GameSprite(260, 100, 60, 70, 15, 'alien.png')
enemy3 = GameSprite(375, 100, 60, 70, 12, 'alien.png')
enemy4 = GameSprite(430, 100, 60, 70, 14, 'alien.png')
enemy5 = GameSprite(560, 100, 60, 70, 11, 'alien.png')
enemy6 = GameSprite(595, 100, 60, 70, 13, 'alien.png')
enemy7 = GameSprite(30, 100, 60, 70, 13, 'alien.png')

# настройка игровых переменных
lives = 15
counter = 0
seconds = 50

# создание шрифта
font.init()
font1 = font.Font(None, 43)

# creating a groups of sprites
enemies = [enemy, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7]
bullets = sprite.Group()

# startin the game timer
start = timer()

# main loop value
game = True

'''
дальше идет игровой цикл.
время может считаться довольно странно,
но я позже это исправлю
'''

# main loop
while game:
    # timestamp for the game timer
    stop = timer()

    window.blit(background, (0, 0))
    lives_text = font1.render('Жизни;D:'+ str(lives), 1, (10, 10, 10))
    window.blit(lives_text, (480, 100))

    counter_text = font1.render('Убито:'+ str(counter), 1, (10, 10, 10))
    window.blit(counter_text, (480, 160))

    seconds_text = font1.render('Время:'+ str(seconds), 1, (10, 10, 10))
    window.blit(seconds_text, (480, 60))

    if stop - start > 1:
        seconds -= 1
        start = stop


    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                lives = 25
                counter = 0
                seconds = 50
                rocket.speed = 14
                for enemy in enemies:
                    enemy.rect.y = -10
                    enemy.speed = randint(10,25)
                      
            if e.key == K_SPACE:
                bullet = GameSprite(rocket.rect.x + 20, rocket.rect.y, 10, 20, 15, 'bullet.png')
                bullets.add(bullet)

    if enemy.rect.y > 700:
        enemy.rect.y = 10
        enemy.speed = randint(10,25)

    if enemy2.rect.y > 700:
        enemy2.rect.y = 10
        enemy2.speed = randint(10,25)

    if enemy3.rect.y > 700:
        enemy3.rect.y = 10
        enemy3.speed = randint(10,25)

    if enemy4.rect.y > 700:
        enemy4.rect.y = 10
        enemy4.speed = randint(10,25)

    if enemy5.rect.y > 700:
        enemy5.rect.y = 10
        enemy5.speed = randint(10,25)

    if enemy6.rect.y > 700:
        enemy6.rect.y = 10
        enemy6.speed = randint(10,25)

    if enemy7.rect.y > 700:
        enemy7.rect.y = 10
        enemy7.speed = randint(10,25)

    for enemy in enemies:
        if sprite.collide_rect(rocket, enemy):
            lives -= 1
            counter += 1
            enemy.rect.x = randint(50,650)
            enemy.rect.y = 10

    for bullet in bullets:
        bullet.bullet_update()

    if lives <= 0:
        lose_text = font1.render('ВЫ ПРОИГРАЛИ :(', 1, (255,255,255))
        restart_text = font1.render('Нажмите R, чтобы начать заново', 1, (255,255,255))
        window.blit(lose_text, (250, 150))
        window.blit(restart_text, (180, 170))
        seconds = 50
        for enemy in enemies:
            enemy.speed = 0
        rocket.speed = 0
        for bullet in bullets:
            bullet.kill()    

    if seconds <= 0:
        if counter >= 25:
            win_text = font1.render('ВЫ ВЫИГРАЛИ:)', 1, (255,255,255))
            restart_text = font1.render('Нажмите R, чтобы начать заново', 1, (255,255,255))
            window.blit(restart_text, (180, 170))
            window.blit(win_text, (250, 150))
            seconds = 51
            for enemy in enemies:
                enemy.speed = 0
            rocket.speed = 0
        else:
            win_text = font1.render('ВЫ ПРОИГРАЛИ:(', 1, (255,255,255))
            restart_text = font1.render('Нажмите R, чтобы начать заново', 1, (255,255,255))
            window.blit(restart_text, (180, 170))
            window.blit(win_text, (250, 150))
            seconds = 51 
            for enemy in enemies:
                enemy.speed = 0
            rocket.speed = 0
            for bullet in bullets:
                bullet.kill()

    # when bullet meets enemy
    for enemy in enemies:
        for bullet in bullets:
            if sprite.collide_rect(enemy, bullet):
                enemy.rect.x = randint(50,650)
                enemy.rect.y = -10
                enemy.speed = randint(6,11)
                counter += 1
                bullet.kill()


    rocket.rocket_update()
    enemy.enemy_update()
    enemy2.enemy_update2()
    enemy3.enemy_update3()
    enemy4.enemy_update4()
    enemy5.enemy_update5()
    enemy6.enemy_update6()
    enemy7.enemy_update7()
    rocket.reset()
    enemy.reset()
    enemy2.reset()
    enemy3.reset()
    enemy4.reset()
    enemy5.reset()
    enemy6.reset()
    enemy7.reset()
    bullets.draw(window)
    display.update()
    time.delay(50)
