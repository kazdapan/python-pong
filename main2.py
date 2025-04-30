import pygame
import random

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

player1score = 0
player2score = 0

font = pygame.font.SysFont("Comic Sans MS", 30)

is1MovingUp = False
is1MovingDown = False
is2MovingDown = False
is2MovingUp = False

player1PosX = 5
player1PosY = 300

player2PosX = 770
player2PosY = 300

pygame.display.set_caption("Pong")


class Ball:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.direction = [random.randint(0, 1), random.randint(0, 1)]
        self.speed = [5, random.uniform(5, 5)]

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

    def switchDirection(self):
        self.direction[0] = not self.direction[0]
        self.direction[1] = not self.direction[1]
        self.speed = [5, random.uniform(5, 5)]

    def bounce(self):
        self.direction[1] = not self.direction[1]
        self.speed = [5, random.uniform(5, 5)]

    def move(self):
        if self.direction[0]:
            self.x += self.speed[0]
        else:
            self.x -= self.speed[0]
        if self.direction[1]:
            self.y += self.speed[1]
        else:
            self.y -= self.speed[1]

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def boundaries(self):
        if ball.x <= 0:
            self.switchDirection()
        if ball.x + self.size >= 800:
            self.switchDirection()
        if ball.y + self.size >= 600:
            self.bounce()
        if ball.y <= 0:
            self.bounce()


ball = Ball(400, 250, (255, 255, 255), 15)

while running:

    text_surface1 = font.render('Player 1 Score: ' + str(player1score), False, (255, 255, 255))
    text_surface2 = font.render('Player 2 Score: ' + str(player2score), False, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                is1MovingUp = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                is1MovingUp = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                is1MovingDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                is1MovingDown = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                is2MovingUp = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                is2MovingUp = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                is2MovingDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                is2MovingDown = False

    rect = pygame.Rect((player1PosX, player1PosY), (25, 100))
    rect2 = pygame.Rect((player2PosX, player2PosY), (25, 100))

    if is1MovingUp == True:
        player1PosY -= 10
    if is1MovingDown == True:
        player1PosY += 10

    if is2MovingUp == True:
        player2PosY -= 10
    if is2MovingDown == True:
        player2PosY += 10

    if player1PosY == 510:
        player1PosY = 500
    if player1PosY == -10:
        player1PosY = 0

    if player2PosY == 510:
        player2PosY = 500
    if player2PosY == -10:
        player2PosY = 0

    if rect.colliderect(ball.getRect()):
        ball.switchDirection()
        player1score + 1
    if rect2.colliderect(ball.getRect()):
        ball.switchDirection()
        player2score + 1

    #RENDERING

    #BG
    screen.fill("black")
    #Text
    screen.blit(text_surface1, (100, 50))
    screen.blit(text_surface2, (450, 50))
    #PlayerRender
    ball.draw(screen)
    ball.boundaries()
    ball.move()
    pygame.draw.rect(screen, "white", rect)
    pygame.draw.rect(screen, "white", rect2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
