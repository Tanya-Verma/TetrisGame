import pygame
import random

#intiating pygame

pygame.init()



#created the game screen of aspect ratio of 
#defined column and rows of screen
#intialised the BLOCK size to 30
#math to calculate the number of columns and rows in the game screen
WIDTH,HEIGHT =300,600
BLOCK=30
COLS=WIDTH//BLOCK
ROWS=HEIGHT//BLOCK




screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tetris")


#defined the colors and shapes for tetris pieces





