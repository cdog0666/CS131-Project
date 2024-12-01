import threading

import pygame
import random
import time

#Array Setup
array1 = []
arraySize = 1000
for x in range(0,arraySize):
    array1.append(random.randint(1,100))

# pygame setup
FPS = 60
WIDTH,HEIGHT = 1280,720
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Algo Race")

#SortingFunctions
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            time.sleep(0.0001)

def draw_array(array,window, color):
    y=0
    for x in array:
        pygame.draw.rect(window,color,pygame.Rect(y,HEIGHT-7*x,WIDTH/arraySize,7*x))
        y += WIDTH/arraySize

#Main
def draw_window():
    WIN.fill("BLACK")
    draw_array(array1,WIN,"Blue")
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    clock.tick(FPS)
    sorting_thread = threading.Thread(target=bubblesort, args=(array1,))
    sorting_thread.start()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()

#Run
if __name__=="__main__":
    main()



