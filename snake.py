import pygame
from random import randint

pygame.init()


WIDTH = 480
HEIGHT = 480

WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255,0,0)
FPS = 10
SCORE = 0

def generateRandomFood() :
    while True:
        x = randint(0,WIDTH) // 20 * 20
        y = randint(0, HEIGHT) // 20 * 20
        if (x,y) not in snake_body:
            return (x,y)

snake_body = [
    (240, 240)
]

snake_x, snake_y = 240, 240
delta_x = 20
delta_y = 0
snake_size = 4

food = generateRandomFood()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font32 = pygame.font.SysFont('Arial', 32) #initialize font style
font18 = pygame.font.SysFont('Arial', 18)

#game over text
GameOverText = font32.render('Game Over', True, RED)




clock = pygame.time.Clock()

running = True
while running:

    screen.fill(BLACK)

    #print food
    pygame.draw.rect(screen, RED, [food[0], food[1], 20, 20])

    #print snake
    for x,y in snake_body:
        pygame.draw.rect(screen, GREEN, [x, y, 20, 20])

   

    if food in snake_body:
        snake_size += 1
        SCORE += 1
        food = generateRandomFood()

    snake_x = (snake_x + delta_x) % WIDTH
    snake_y = (snake_y + delta_y) % HEIGHT 

    if (snake_x, snake_y) in snake_body:
        screen.blit(GameOverText, (250, 250))
        running = False
    

    snake_body.append((snake_x, snake_y))
    
    if len(snake_body) > snake_size:
        snake_body.pop(0)
    
    ScoreText = font18.render('Score : '+str(SCORE), True, WHITE)
    screen.blit(ScoreText, (380, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and delta_y != 20:
                delta_x = 0
                delta_y = -20
            if event.key == pygame.K_DOWN and delta_y != -20:
                delta_x = 0
                delta_y = 20
            if event.key == pygame.K_LEFT and delta_x != 20:
                delta_x = -20
                delta_y = 0
            if event.key == pygame.K_RIGHT and delta_x != -20:
                delta_x = 20
                delta_y = 0


    

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

