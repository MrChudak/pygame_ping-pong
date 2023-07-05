import pygame
from random import choice

pygame.init()
pygame.font.init()

loop = True
finish = False
FPS = 60
tick = 0
WIDTH = 700
HEIGHT = 500
background_game = (0, 162, 135)
background_end = (103, 227, 0)
count_l = 0
count_r = 0
ball_speed = [-2, -1, 1, 2]
start = False
second = 100
animation = False
BLUE = (0, 0, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping-pong')


# s = pygame.sprite.Sprite()
class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       screen.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    # def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
    #     super().__init__(player_image, player_x, player_y, player_speed, wight, height)


    def update_r(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if self.rect.y >= 5:
                self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.rect.y <= 400:
                self.rect.y += self.speed


    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.y >= 5:
                self.rect.y -= self.speed
        if keys[pygame.K_s]:
            if self.rect.y <= 400:
                self.rect.y += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_image, ball_x, ball_y, ball_speed_x, ball_speed_y, wight, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(ball_image), (wight, height)) #вместе 55,55 - параметры
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = ball_x
        self.rect.y = ball_y

    def reset(self):
       screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (pygame.sprite.collide_rect(self, right_pad) and self.speed_x > 0) or  (self.speed_x < 0 and pygame.sprite.collide_rect(self, left_pad)):
            self.speed_x *= -1
            self.speed_x *= 1.2
            self.speed_y *= 1.2
            print('speed:', self.speed_x, self.speed_y)

        if (self.rect.y <= 5 and self.speed_y < 0) or (self.rect.y >= 475 and self.speed_y > 0):
            self.speed_y *= -1
        


right_pad = Player('pad.png', 640, 200, 5, 25,100)

left_pad = Player('pad.png', 10, 200, 5, 25,100)

ball = Ball('pad.png', 325, 225, 0, 0, 25,25)


font_int = pygame.font.Font(None, 40)
font_button = pygame.font.Font(None, 40)
font_count = pygame.font.Font(None, 70)


text_int = font_int.render('Для старта нажмите: ', True, (0,0,0))
text_button = font_button.render('"Пробел"', True, (0,0,0))
text_second = font_int.render(str(second), True, (0, 0, 0))


text_count_l = font_count.render(str(count_l), True, (0,0,0))
text_count = font_count.render(':', True, (0,0,0))
text_count_r = font_count.render(str(count_r), True, (0,0,0))

text_goal = font_count.render('GOAL!!!', True, BLUE)

text_win_l = font_int.render('Игрок слева победил!', True, (0, 0, 0))
text_win_r = font_int.render('Игрок справа победил!', True, (0,0,0))
nobody = font_int.render('Победитель не выявлен!', True, (0, 0, 0))



while loop:
    
    while not finish:
        clock.tick(FPS)
        screen.fill(background_game)

        if not start:
            screen.blit(text_int, (200,100))
            screen.blit(text_button, (260, 150))
            screen.blit(text_count_l, (280, 50))
            screen.blit(text_count, (330, 50))
            screen.blit(text_count_r, (380, 50))
            screen.blit(text_second, (330, 10))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                start = True
                ball.speed_y = choice(ball_speed)
                ball.speed_x = choice(ball_speed)

        else:
            screen.blit(text_count_l, (280, 50))
            screen.blit(text_count, (330, 50))
            screen.blit(text_count_r, (380, 50))
            screen.blit(text_second, (330, 10))
            if tick >= 60:
                second -= 1
                tick = 0
                text_second = font_int.render(str(second), True, (0, 0, 0))
        


        if ball.rect.x >= 700:
            count_l += 1
            start = False
            ball.speed_x, ball.speed_y = 0, 0
            ball.rect.y, ball.rect.x = 225, 325
            text_count_l = font_count.render(str(count_l), True, (0,0,0))
            animation = True
        
        elif ball.rect.x <= 0:
            count_r += 1
            start = False
            ball.speed_x, ball.speed_y = 0, 0
            ball.rect.y, ball.rect.x = 225, 325
            text_count_r = font_count.render(str(count_r), True, (0,0,0))
            animation = True
            

        
        if animation:
            while tick <= 60 * 2:
                clock.tick(FPS)
                screen.fill(background_game)
                tick += 1
                screen.blit(text_goal, (300, 250))
                if tick % 10 == 0:
                    text_goal = font_int.render('GOAL!!!', True, RED)
                    
                elif tick % 5 == 0:
                    text_goal = font_int.render('GOAL!!!', True, BLUE)

                pygame.display.update()
            
                for even in pygame.event.get():
                    if even.type == pygame.QUIT:
                        finish = True

            animation = False
                


    
        

        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                finish = True
        

        right_pad.reset()
        left_pad.reset()
        ball.reset()

        right_pad.update_r()
        left_pad.update_l()
        ball.update()
        



        if second <= 0 or count_l == 5 or count_r == 5:
            finish = True

        for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    finish = True

        tick += 1
        pygame.display.update()




    clock.tick(FPS)
    screen.fill(background_end)

    if count_r > count_l:
        screen.blit(text_win_r, (240, 240))

    elif count_r < count_l:
        screen.blit(text_win_l, (240, 240))
    else:
        screen.blit(nobody, (240, 240))


    for even in pygame.event.get():
            if even.type == pygame.QUIT:
                loop = False
    pygame.display.update()
