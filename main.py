import pygame

pygame.init()

loop = True
finish = False
FPS = 60
tick = 0
WIDTH = 700
HEIGHT = 500
background_game = (0, 162, 135)
backgroun_end = (103, 227, 0)
second = 0

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
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)


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
    def __init__(self, ball_image, ball_x, ball_y, ball_speed_x, bal    l_speed_y, wight, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(ball_image), (wight, height)) #вместе 55,55 - параметры
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = ball_x
        self.rect.y = ball_y


    def update(self):
        self.rect.x += ball_speed_x
        self.rect.y += ball_speed_y
        if rectcollide(self, right_pad):
            self.rect.x = -ball_speed_x


right_pad = Player('pad.png', 640, 15, 5, 25,100)

left_pad = Player('pad.png', 10, 15, 5, 25,100)

ball = Ball('pad.png', 100, 100, 5,5, 25,25)



while loop:
    
    while not finish:
        clock.tick(FPS)
        screen.fill(background_game)
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                finish = True
        if tick % 60 == 0:
            second += 1

        right_pad.reset()
        left_pad.reset()
        ball.reset()

        right_pad.update_r()
        left_pad.update_l()
        ball.update()
        



        tick += 1

        for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    finish = True


        pygame.display.update()


    for even in pygame.event.get():
            if even.type == pygame.QUIT:
                loop = False


    clock.tick(FPS)
    screen.fill(background_end)
    pygame.display.update()