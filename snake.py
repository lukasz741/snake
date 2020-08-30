import pygame
pygame.init()
import random

win = pygame.display.set_mode((500,550))

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

class snake():
    def __init__(self,x,y,a,b):
        self.x = x
        self.y =y
        self.a =a
        self.b = b


class objectFood():
    def __init__(self,x,y,a,b):
        self.x = x
        self.y =y
        self.a =a
        self.b = b

    # def draw(self,win):
    #     pygame.draw.rect(win, (255, 0, 0), (x, y, a, b)


def redrawGameWindow():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0,255,0), (food.x, food.y,food.a,food.b))
    for i in snaketail:
        pygame.draw.rect(win, (255, 255, 0), (i.x, i.y, i.a, i.b))
    # snakehead.draw(win)
    pygame.draw.line(win, (255, 255, 255), (0, 500), (500, 500))
    text = font.render("Score: " + str(score), 1, (255, 255, 255))  # rendering new text
    win.blit(text, (350, 510))  # position of text in gui
    pygame.display.update()

def redrawGameWindowTest():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0,255,0), (food.x, food.y,food.a,food.b))
    pygame.draw.rect(win, (255, 255, 255), (superfood.x, superfood.y, superfood.a, superfood.b))
    for i in snaketail:
        pygame.draw.rect(win, (80, 150, 100), (i.x, i.y, i.a, i.b))
    # snakehead.draw(win)
    pygame.draw.line(win,(255,255,255), (0,500),(500,500))
    text = font.render("Score: " + str(score), 1, (255, 255, 255))  # rendering new text
    win.blit(text, (350, 510))  # position of text in gui
    pygame.display.update()


def correctSnakeLength():
    if len(snaketail)>foodCounter:
        snaketail.pop(0)

def snakeCollision():
    global run
    for i in snaketail[2:]:
        if newsnake.x == i.x and newsnake.y == i.y:
            run = False

#mainloop
font = pygame.font.SysFont("arial", 30,True) #fontname, size, bold T/f,
snakehead=snake(0,0,10,10)
snaketail = []
snaketail.append(snakehead)
food = objectFood(random.randint(4, 496), random.randint(4, 496), 10, 10)
superfood = objectFood(random.randint(4, 496), random.randint(4, 496), 15, 15)
x_change = 0
y_change = 0
foodCounter =1
variablefood = 1
score = 0
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change!=10:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change!=-10:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP and y_change!=10:
                x_change = 0
                y_change = -10
            elif event.key == pygame.K_DOWN and y_change!=-10:
                x_change = 0
                y_change = 10

    snakehead.x += x_change
    snakehead.y +=y_change
    newsnake=snake(snakehead.x,snakehead.y,10,10)
    snakeCollision()
    snaketail.append(newsnake)


    if snakehead.x not in range(0,500) or snakehead.y not in range(0,500):
        run = False

    # hit loop:
    if food.y - food.b < snakehead.y + snakehead.b and food.y + food.b > snakehead.y:
        if food.x + food.a > snakehead.x and  food.x-food.a < snakehead.x + snakehead.a:
            del food
            food = objectFood(random.randint(4, 496), random.randint(4, 496), 10, 10)
            foodCounter +=1
            score +=1

    if foodCounter %5 ==0:
        variablefood=2
    else:
        variablefood=1

    correctSnakeLength()
    if variablefood ==1:
        redrawGameWindow()
    if variablefood ==2:
        if superfood.y - superfood.b < snakehead.y + snakehead.b and superfood.y + superfood.b > snakehead.y:
            if superfood.x + superfood.a > snakehead.x and superfood.x - superfood.a < snakehead.x + snakehead.a:
                del superfood
                superfood = objectFood(random.randint(4, 496), random.randint(4, 496), 15, 15)
                foodCounter += 1
                score += 3
        redrawGameWindowTest()

    clock.tick(25)

pygame.quit()

if run == False:
    print("\nYour score was: " +str(score))