#Создай собственный Шутер!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed



window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
clock = time.Clock()
FPS = 60
win_width = 700
win_height = 500

back = (200,255,255)
window.fill(back)

game = True
finish = False


speed = 2

font.init()
font1 = font.SysFont('Arial', 40)
score = 0  # сбито



mixer.init()  
mixer.music.load('space.ogg')  
mixer.music.play()
fire = mixer.Sound('fire.ogg')
fall = mixer.Sound('fall.ogg')



igrok1 = Player("Racket2.0.png", 30 , 200 , 50, 150,4)
igrok2 = Player("Racket2.0.png", 620 , 200 , 50, 150,4)
ball = GameSprite('asteroid.png', 200, 200, 50, 50, 4)

lose1 = font1.render("ПРОИГРЫШ! Игрок 1", True, (255, 0, 0))
lose2 = font1.render("ПРОИГРЫШ! Игрок 2", True, (0, 255, 0))

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type ==  QUIT:
            game = False
                    
    if not finish:
        window.fill(back)
        igrok1.update_l()
        igrok2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(igrok1, ball) or sprite.collide_rect(igrok2, ball):
           speed_x *= -1
           speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
           speed_y *= -1

        if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True
        
        if ball.rect.x > win_width:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True

        igrok1.reset()
        igrok2.reset()
        ball.reset()

        display.update()
    clock.tick(FPS)


  












'''
monsters = sprite.Group()
monsters.add(monster)
monsters.draw(window)


локальная область видимость=видимость внутри некоторого блока кода
глоб переменная=переменная областью видимости которой явлвся программа

Метод = функция внутри обьекта
наследование перенести все умения для более общего класса
свойство поле= переменная внутри обьекта
класс = единое название для многих обьектов
классы = готовые уже в библиотеке
игровой цикл = спрайты,их нахождение 


bullet = kill()


mixer.init()  
mixer.music.load('jungles.ogg')  
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = 'left'

    def update(self):
        if self.rect.x <= 470: 
            self.direction = 'right'
        if self.rect.x > 700 - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        self.color_1 = color_1 
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



wall1 = Wall(82, 2, 242, 470, 100, 10 , 500)
wall2 = Wall(82, 2, 242, 100, 100, 10 , 500)
wall3 = Wall(82, 2, 242, 290, 0, 10 , 350)

'фон игры'
background = transform.scale(image.load("background.jpg"), (700, 500))

hero = Player('hero.png', x1, y1, 2)

final = GameSprite('treasure.png', 600, 420, 0)
monster = Enemy('cyborg.png', x2, y2, 2)

создание текстового оповещения
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (0,255,0))
lose = font.render('YOU LOSE!', True, (255,0,0))

game = True
finish = False
while game:

    for e in event.get():
        if e.type ==  QUIT:
            game = False
        if finish != True:
            window.blit(background,(0, 0))
            wall1.draw_wall()
            wall2.draw_wall()
            wall3.draw_wall()
            hero.reset()
            hero.update()
            monster.reset()
            monster.update()
            final.reset()
            if sprite.collide_rect(hero, final):
                window.blit(win, (200, 200))
                finish = True
                money.play()
            if sprite.collide_rect(hero, monster) or sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2)or sprite.collide_rect(hero, wall3):
                window.blit(lose, (200, 200))
                finish = True
                kick.play()
            


    keys_pressed = key.get_pressed()

    if keys_pressed[K_w]:
        y1  -= speed

    if keys_pressed[K_s] and y2 < 595:
        y2  += speed

    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= speed

    if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += speed

    if keys_pressed[K_UP] and y1 > 0:
        y1 -= speed

    if keys_pressed[K_DOWN] and y1 < 400:
        y1 += speed'''
'''
    display.update()
    clock.tick(FPS)
display.update() 


класс  wall = конструктор = вызов констр спрайт
цвет три поля
длина и ширрина стены


image = Surface((width, height))  создает обьект сурфейс

image.fill((color_1, color_2, color_3))

rect = image.get_rect()   возвращает обьект рект прямоугл-ю подложку спрайта

class wall(sprite.sprite):
    def __init__(self, color_1 2 3,  wall_x wall_y wall_width):
        self.color_1 = color_1n2n3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.
        self.


class Player(GameSprite):
    def update(self):
        key = key.get_pressed()
        if keys_pressed[K_w]:
        y1  -= speed

       if keys_pressed[K_s] and y2 < 595:
        y2  += speed

        if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= speed

         if keys_pressed[K_RIGHT] and x1 < 600:
        x1 += speed

           if keys_pressed[K_UP] and y1 > 0:
        y1 -= speed

          if keys_pressed[K_DOWN] and y1 < 400:
        y1 += speed



game = True
while game:

    for e in event.get():
        if e.type ==  QUIT:
            game = False
    window.blit(background,(0, 0))
    hero.reset()
    monster.reset()
    final.reset()


class назв класса():
    def __init__(self, значение):
        self.Название свойства= значение
    def назв метода (self):
        действие с обьектом и свойствами


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))


mixer.init() = подключение возможности использовать миксер
mixer.music.load('Название музыки.ogg') = загрузка музыкового файла
mixer.music.play()
kick = mixer.sound('') = воспроизвести одноразово звук
kick.play() = Воспроизвести звук
keys_pressed = key.get_pressed()  взвращает структуру с тек состоянием клавиш тру опущена а фолс поднята
if keys_pressed[K_UP]:
    y1 -= 10 если клавиша стрелка вверх опущенато уменьшить координату у спрайт1 на 10  пикселей
наследование = помогает перенести все умения написанные ранее для более общего класса Пример: A свойство методы < Свойство методы B
                                                                                             + свойства методы 
'''