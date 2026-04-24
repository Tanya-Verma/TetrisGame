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
            pygame.draw.rect(screen, (40, 40, 40),(x * BLOCK, y * BLOCK, BLOCK, BLOCK), 1, )

def draw_block():
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x],(x*BLOCK,y*BLOCK,BLOCK,BLOCK))
                

'''Created a class to represent the tetris pieces, which will have attributes for the shape,
 color, and position of the piece on the grid.
 The class will also have methods for moving and rotating the piece.'''

class Piece:
    def __init__(self):
        self.figure=random.choice(SHAPES)
        self.color=random.choice(COLORS)
        self.x=COLS//2-len(self.figure[0])//2
        self.y=0
        self.width=COLS
        self.height=ROWS
        self.grid=grid
# making draw, rotate, move, and collision methods for the Piece class

    def draw(self):
        for i,row in enumerate(self.figure):
            for j,val in enumerate(row):
                if val:
                    pygame.draw.rect(screen,self.color,((self.x+j)*BLOCK,(self.y+i)*BLOCK,BLOCK,BLOCK))
        
    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.figure=[list(row) for row in zip(*self.figure[::-1])]
        

    def collision(self,dx,dy):
        for i,row in enumerate(self.figure):
            for j,val in enumerate(row):
                if val:
                    if i + self.y > self.height - 1 or j + self.x < 0 or j + self.x > self.width - 1 or (self.y + i >= 0 and self.grid[self.y + i][self.x + j]):
                        return True
        return False
    
    def merge(piece):
        for i,row in enumerate(piece.figure):
            for j,val in enumerate(row):
                if val:
                    grid[piece.y + i][piece.x + j]=piece.color


    def clear_lines():
        global grid
        new_grid=[row for row in grid if any(cell ==0 for cell in row)]
        lines_cleared=ROWS-len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(COLS)])
        grid=new_grid


#main game loop







  


 


                
    















