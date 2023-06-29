import pygame

pygame.init()

loop = True
finish = False
FPS = 60
tick = 0
WIDTH = 700
HEIGHT = 500
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = (255, 255, 255)
second = 0


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

        if keys[pygame.KEYDOWN.k_UP]:
            if self.rect.y >= 5:
                self.rect.y -= self.speed

        if keys[k_DOWN]:
            if self.rect.y <= 400:
                self.rect.y += self.speed


    def update_l(self):
        if keys[k_w]:
            if self.rect.y >= 5:
                self.rect.y -= self.speed
        if keys[k_s]:
            if self.rect.y <= 400:
                self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)


    def update(self):
        pass


right_pad = Player('pad.png', 640, 15, 5, 25,100)

left_pad = Player('pad.png', 10, 15, 5, 25,100)

ball = Ball('pad.png', 100, 100, 5, 25,25)



while loop:
    
    while not finish:
        clock.tick(FPS)
        screen.fill(background)
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
    screen.fill(background)
    pygame.display.update()