import pgzrun
import pygame
import random


WIDTH = 600
HEIGHT = 800

# paddle = pygame.image.load('p_p.jpg')
# paddle = Actor('p_p.jpg')
# paddle.x = 350
# paddle.y = 370

# rewrite with class

# ball = Actor('r_b.png')
# ball.x = 260
# ball.y = 260

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 60
        self.color = (200, 0, 0)

        # self.rect = pygame.Rect(self.x, self.y, 6, 6)
        self.actor = Actor('r_b.png',(x, y))
    def draw(self):
        self.actor.draw()



class Brick:
    def __init__(self, x, y, randomcolor):
        self.x = x
        self.y = y
        self.color = randomcolor
        self.rect = pygame.Rect(self.x, self.y, 50, 20)

    def update(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 20))

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 60
        self.rect = pygame.Rect(self.x, self.y, self.size, 10)

    def update(self):
        pass
        # paddle = pygame.image.load('p_p.jpg')
        # pygame.draw.rect(screen, RED, (self.x, self.y, self.size, 10))


paddle = Paddle(350, 370)
# ball = Ball(200, 200)

# paddle = pygame.image.load('p_p.jpg')
# paddle = Actor('p_p.jpg')
# paddle.x = 350
# paddle.y = 370

ball = Ball(250,280)
ball_x_speed = -3
ball_y_speed = 3

bars_list = []

def draw():
    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    screen.clear()
    color = (0, 100, 100)
    surface.fill(color)
    pygame.display.flip()
    screen.draw.rect(paddle.rect, (200,0,0))
    ball.draw()
    # ball.draw()
    # for bar in bars_list:
    #     bar.draw()

def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)

def on_mouse_move(pos):
    x = pos[0]
    paddle.rect.centerx = x

def update(dt):
    global ball_x_speed, ball_y_speed
    # if keyboard.left:
    #     paddle.x = paddle.x - 5
    # if keyboard.right:
    #     paddle.x = paddle.x + 5


    update_ball()
    for bar in bars_list:
        if ball.actor.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1


        # rand = random.randint(0,1)
        # if rand:
        #     ball_x_speed *= -1

def update_ball():
    global ball_x_speed, ball_y_speed

    if (ball.actor.x >= WIDTH) or (ball.actor.x <=0):
        ball_x_speed *= -1
    if (ball.actor.y <=0):
        ball_y_speed *= -1

    if ball.actor.y >= paddle.rect.y:
        if paddle.rect.bottomleft[0] <= ball.actor.x <= paddle.rect.bottomright[0]:
            ball_y_speed *= -1
        else:
            pass
        #lives counter func

    ball.actor.x -= ball_x_speed
    ball.actor.y += ball_y_speed
        
def lives():
    pass



coloured_box_list = ["r_g.jpg", "r_o.jpg","r_p.jpg"]
x = 50
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()
