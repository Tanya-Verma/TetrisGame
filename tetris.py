import pygame
import random

pygame.init()

WIDTH, HEIGHT = 300, 600
BLOCK = 30
COLS = WIDTH // BLOCK
ROWS = HEIGHT // BLOCK

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

COLORS = [
    (0,255,255),
    (255,255,0),
    (255,0,255),
    (0,255,0),
    (255,0,0),
    (0,0,255),
    (255,165,0)
]

SHAPES = [
    [[1,1,1,1]],
    [[1,1,1], [0,1,0]],
    [[1,1,1], [1,0,0]],
    [[1,1,1], [0,0,1]],
    [[1,1], [1,1]],
    [[0,1,1], [1,1,0]],
    [[1,1,0], [0,1,1]]
]

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen, (40,40,40), (x*BLOCK, y*BLOCK, BLOCK, BLOCK), 1)

def draw_block():
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], (x*BLOCK, y*BLOCK, BLOCK, BLOCK))

class Piece:
    def __init__(self):
        self.figure = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS//2 - len(self.figure[0])//2
        self.y = 0
        self.width = COLS
        self.height = ROWS
        self.grid = grid

    def draw(self):
        for i,row in enumerate(self.figure):
            for j,val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, self.color,
                                     ((self.x+j)*BLOCK, (self.y+i)*BLOCK, BLOCK, BLOCK))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.figure = [list(row) for row in zip(*self.figure[::-1])]

    def collision(self, dx=0, dy=0):
        for i,row in enumerate(self.figure):
            for j,val in enumerate(row):
                if val:
                    new_x = self.x + j + dx
                    new_y = self.y + i + dy
                    if new_y > self.height - 1 or new_x < 0 or new_x > self.width - 1 or (new_y >= 0 and self.grid[new_y][new_x]):
                        return True
        return False

    def merge(self):
        for i,row in enumerate(self.figure):
            for j,val in enumerate(row):
                if val:
                    grid[self.y + i][self.x + j] = self.color
    
    score=0
    def clear_lines(self):
        global grid
        new_grid = [row for row in grid if any(cell == 0 for cell in row)]
        lines_cleared = ROWS - len(new_grid)
        self.score += lines_cleared * 100  
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(COLS)])
        grid = new_grid

clock = pygame.time.Clock()
piece = Piece()
running = True
fall_time = 0

while running:
    screen.fill((0,0,0))
    fall_time += clock.get_rawtime()
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                piece.move(-1,0)
                if piece.collision():
                    piece.move(1,0)

            if event.key == pygame.K_RIGHT:
                piece.move(1,0)
                if piece.collision():
                    piece.move(-1,0)

            if event.key == pygame.K_DOWN:
                piece.move(0,1)
                if piece.collision():
                    piece.move(0,-1)

            if event.key == pygame.K_UP:
                piece.rotate()
                if piece.collision():
                    piece.rotate()
                    piece.rotate()
                    piece.rotate()

            if event.key==pygame.K_p:
                paused=not paused


if not paused:
    if fall_time > 500:
        piece.move(0,1)
        if piece.collision():
            piece.move(0,-1)
            piece.merge()
            piece.clear_lines()
            piece = Piece()
            if piece.collision():
                running = False
        fall_time = 0

    draw_block()
    piece.draw()
    draw_grid()

    font_small=pygame.font.SysFont("Arial",25)
    score_text=font_small.render(f"Score:{piece.score}",True,(255,255,255))
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()