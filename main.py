import pygame
import random


#Array Setup
array1 = []
for x in range(0,100):
    array1.append(random.randint(1,100))
array2 = array1

#SortingFunctions
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array



# pygame setup
FPS = 60
WIDTH,HEIGHT = 1280,720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Algo Race")

def draw_array(array,window, color):
    y=0
    for x in array:
        pygame.draw.rect(window,color,pygame.Rect(y,HEIGHT-x,WIDTH/100,x))
        y=y+(WIDTH/100)

#Main
def draw_window():
    WIN.fill("BLACK")
    draw_array(array1,WIN,"blue")
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()

#Run
if __name__=="__main__":
    main()



