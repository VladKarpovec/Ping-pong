from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self, window):  
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self, keys):
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

    def update_r(self, keys):
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
'''class Enemy(GameSprite):
    def update(self):'''

    

winh = 550
winw = 600
window = display.set_mode((winw, winh))
display.set_caption("Пінг-понг")
window.fill((255, 255, 255))

player1 = Player("player.png", 10, 10, 5)
player2 = Player("player.png", 540, 490, 5)
ball = GameSprite("ball.png", 200, 200, 5)

font.init()
font = font.Font(None, 36)
lose_player1 = font.render("PLAYER 1 LOSE", True, (0, 200, 0))
lose_player2 = font.render("PLAYER 2 LOSE", True, (255, 0, 0))

clock = time.Clock()
FPS = 60
game = True
finish = False
speed_x = 3
speed_y = 3

while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill((230,230,255))
        player1.reset(window)
        player2.reset(window)
        player1.update_r(keys)
        player2.update_l(keys)

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if ball.rect.y > winh - 50 or ball.rect.y < 0:
            speed_y *=-1
        if ball.rect.x < 0:
            finish =True
            window.blit(lose_player1, (200,200))
        if ball.rect.x > winw:
            finish =True
            window.blit(lose_player2, (200,200))

        ball.reset(window)
        
    clock.tick(FPS)
    display.update()

