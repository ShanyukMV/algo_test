from pygame import *

#окно игры
win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Пинг понг")

#фон сцены
color_b = (200, 255, 255)
window.fill(color_b)

# ракетки и мяч
class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# ракетки
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y = self.rect.y + self.speed
        
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.y > 5:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_z] and self.rect.y < win_height - 80:
            self.rect.y = self.rect.y + self.speed


r1_x = 30
r1_y = 200
r2_x = 520
r2_y = 200
r_w = 50
r_h = 70
racket1 = Player("racket.png", r1_x, r1_y, 4, r_w, r_h)
racket2 = Player("racket.png", r2_x, r2_y, 4, r_w, r_h)

# мяч
b_x = 200
b_y = 200
ball = GameSprite("tenis_ball.png", b_x, b_y, 4, 50, 50)
ball_step_x = 2
ball_step_y = 2

# Надписи для результатов
font.init()
font = font.Font(None, 35)
winner1 = font.render('Выиграла Ракетка 1', True, (180, 0,0))
winner2 = font.render('Выиграла Ракетка 2', True, (180, 0,0))

game = True
finish = False
clock = time.Clock()
FPS = 60 # частота кадров


while game:    
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    if finish != True:
        window.fill(color_b)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x = ball.rect.x + ball_step_x
        ball.rect.y = ball.rect.y + ball_step_y

        # обработка столкновений
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_step_x = -1 * ball_step_x
            ball_step_y = -1 * ball_step_y

        # мяч достиг границы экрана
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            ball_step_y = -1 * ball_step_y

        # мяч улетел дальше ракетки
        if ball.rect.x < 0:
            finish = True
            window.blit(winner2, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(winner1, (200, 200))

    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
