import pygame
import random

#Array Setup
array1 = []
for x in range(0,100):
    array1.append(random.randint(1,100))
array2 = array1

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
  
    pygame.display.flip()
    clock.tick(60)
pygame.quit()