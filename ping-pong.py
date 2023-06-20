from pygame import *

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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 1420:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < 1420:
            self.rect.y += self.speed

window = display.set_mode((1500 , 1000))
display.set_caption('ping-pong')
background = transform.scale(image.load('background.jpg') , (1500 , 1000))
game = True
while game:
    window.blit(background , (0 , 0))
    
    for e in event.get():
        if e.type == QUIT:
            finish = True
            game = False

    time.delay(60)
    display.update()