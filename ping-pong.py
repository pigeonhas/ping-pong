from pygame import *

game = True
l_score = 0
r_score = 0

class Gamesprite(sprite.Sprite):
    def __init__(self , player_speed , player_x , player_y , player_image , weight , height):
        sprite.Sprite.__init__(self)
        self.weight = weight
        self.height = height
        self.image = transform.scale(image.load(player_image) , (self.weight , self.height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))

class Player(Gamesprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 9:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 800:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 9:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 800:
            self.rect.y += self.speed

class Enemy(Gamesprite):
    def update(self):
        global l_score
        global r_score
        if self.rect.x > 1400:
            self.rect.y = 490
            self.rect.x = 740
            l_score += 1
        elif self.rect.x < 10:
            self.rect.y = 490
            self.rect.x = 740
            r_score += 1


window = display.set_mode((1500 , 1000))
display.set_caption('ping-pong')
clock = time.Clock()

background = transform.scale(image.load('background.jpg') , (1500 , 1000))
rocket_l = Player(20 , 109 , 400 , 'racket.png' , 100 , 200)
rocket_r = Player(20 , 1290 , 400 , 'racket.png' , 100 , 200)
ball = Enemy(15 , 740 , 490 , 'tenis_ball.png' , 60 , 60 )

font.init()
font1 = font.SysFont('Bahnschrift' , 60 )

while game:
    text_l = font1.render(str(l_score) , 1 , (0 , 0 , 0))
    text_r = font1.render(str(r_score) , 1 , (0 , 0 , 0))

    window.blit(background , (0 , 0))
    window.blit(text_l , (10 , 10))
    window.blit(text_r , (1460 , 10))
    rocket_l.update_l()
    rocket_r.update_r()
    ball.update()
    rocket_r.reset()
    rocket_l.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(80)
    display.update()