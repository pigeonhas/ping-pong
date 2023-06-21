from pygame import *

game = True
finish = False
l_score = 0
r_score = 0
speed_x = 3
speed_y = 3
winner = ''

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
        global speed_x
        global speed_y
        global timer
        if self.rect.x > 1400:
            self.rect.y = 490
            self.rect.x = 740
            l_score += 1
            if speed_x < 0:
                speed_x = 7
            else:
                speed_x = -7
            if speed_y < 0:
                speed_y = 7
            else:
                speed_y = -7
            speed_x *= -1
            timer = 0
            
        elif self.rect.x < 10:
            self.rect.y = 490
            self.rect.x = 740
            r_score += 1
            speed_x *= -1
            timer = 0

window = display.set_mode((1500 , 1000))
display.set_caption('ping-pong')
clock = time.Clock()

background = transform.scale(image.load('background.jpg') , (1500 , 1000))
rocket_l = Player(20 , 109 , 400 , 'racket.png' , 70 , 210)
rocket_r = Player(20 , 1290 , 400 , 'racket.png' , 70 , 210)
ball = Enemy(15 , 740 , 490 , 'tenis_ball.png' , 60 , 60 )
button = Gamesprite(0 , 740 , 600 , 'button.png' , 60 , 60)

font.init()
font1 = font.SysFont('Bahnschrift' , 60 )

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x , y = e.pos
            if button.rect.collidepoint(x,y):
                finish = False
                l_score = 0
                r_score = 0
                winner = ''
    
    window.blit(background , (0 , 0))
    if r_score > 2 or l_score > 2:
        finish = True
        if r_score > 2:
            winner = 'Player2'
        elif l_score > 2:
            winner = 'Player1'
    if not finish:
        
        ball.rect.y += speed_y
        ball.rect.x += speed_x

        if ball.rect.y > 940 or ball.rect.y < 10:
            speed_y *= -1
        if sprite.collide_rect(rocket_l , ball) or sprite.collide_rect(rocket_r , ball):
            if ball.rect.x < 1240 and ball.rect.x > 160:
                speed_x *= -1
                speed_x *= 1.1
                speed_y *= 1.1
        text_l = font1.render(str(l_score) , 1 , (0 , 0 , 0))
        text_r = font1.render(str(r_score) , 1 , (0 , 0 , 0))
        text_win = font1.render('Победитель:' + winner , 1 , (12 , 255 , 0))

        
        window.blit(text_l , (10 , 10))
        window.blit(text_r , (1460 , 10))
        rocket_l.update_l()
        rocket_r.update_r()
        ball.update()
        rocket_r.reset()
        rocket_l.reset()
        ball.reset()

    
    else:
        button.reset()
        text_win = font1.render('Победитель:' + winner , 1 , (12 , 255 , 0))
        window.blit(text_win , (570 , 490))
        
    clock.tick(30)
    display.update()