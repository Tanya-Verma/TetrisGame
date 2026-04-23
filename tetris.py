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

COLORS =[
    (0,255,255), #cyan
    (255,255,0), #yelllow
    (255,0,255), #magenta
    (0,255,0),   #green
    (255,0,0),   #red
    (0,0,255),   #blue
    (255,165,0)  #orange
    ]

SHAPES=[
    [[1,1,1,1]],  # I
    [[1,1,1], [0,1,0]],  # T
    [[1,1,1], [1,0,0]],  # L
    [[1,1,1], [0,0,1]],  # J
    [[1,1], [1,1]],  # O
    [[0,1,1], [1,1,0]],  # S
    [[1,1,0], [0,1,1]]   # Z
]

#created a grid to represent the game state, initialized with zeros
#instead of using a 2D list, we can use a single list to represent the grid, 
# where each element corresponds to a cell in the grid


grid=[[0 for _ in range(COLS)] for _ in range(ROWS)]

#defined the border of the grid to prevent pieces from moving outside the game area

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(
                screen,
                (40, 40, 40),
                (x * BLOCK, y * BLOCK, BLOCK, BLOCK),
                1,
            )

def draw_block():
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x]!=0:
                pygame.draw.rect(
                    screen,
                    grid[y][x],

                )

class Piece:
    def __init__(self):
        self.figure(random.randint(0,

















