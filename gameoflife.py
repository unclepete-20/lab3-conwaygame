# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Creado por: Pedro Pablo Arriola Jimenez (20188)   
# Fecha de creación: 28/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Laboratorio 3: Conway's Game of Life""" 
# ---------------------------------------------------------------------------

# Imports
import pygame
from numpy import *
from OpenGL.GL import *
import time
from random import *

# Colors
bg = (0.1, 0.1, 0.1)
grid = (0.18, 0.16, 0.19)
color_alive_next = (1, 1, 1)

def rules(cells, size, moving = False):
    update_cells = zeros((cells.shape[0], cells.shape[1]))

    for row, col in ndindex(cells.shape):
        alive = sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
        color = bg if cells[row, col] == 0 else color_alive_next

        # Checks for neighbors
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if moving:
                    color = bg
            elif 2 <= alive <= 3:
                update_cells[row, col] = 1
                if moving:
                    color = color_alive_next
        else:
            if alive == 3:
                update_cells[row, col] = 1
                if moving:
                    color = color_alive_next
        pixel((col * size), (row * size), (size - 1),(size - 1), color)

    return update_cells

def pixel(x, y, w, h, color):
    
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, w, h)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

# Defined patterns and random ones to make the game interesting
patterns = [
    
    [50,100],[60,100],[70,100], #Blinker
    
    
    [80,180],[90,180],[100,180],[90,190],[100,190],[110,190], #Toad
    
    
    [180,150],[190,150],[200,150],[200,160],[190,170], #Glider
    
    
    [200,50],[210,50],[220,60],[210,70],[200,70],[190,60], #Bee-hive
    
    
    [100,300],[110,300],[100,310],[110,310],[120,320],[130,320],[120,330],[130,330], #Beacon
    
    
    [500,350],[510,350],[520,350],[530,350],[490,360],[500,360],[510,360],[520,360],
    [530,360],[540,360],[490,370],[500,370],[510,370],[520,370],[540,370],[550,370],
    [530,380],[540,380], #Heavy Weight Spaceship
    
    # RANDOM PATTERNS
    
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],
    [randint(100, 500), randint(40, 450)], [randint(100, 500), randint(95, 375)], [randint(250, 500), randint(150, 500)],

]

def main():
    # Initializes the screen
    pygame.init()
    pygame.display.set_mode(
    (600, 600),
    pygame.OPENGL | pygame.DOUBLEBUF,
    )
    pygame.display.set_caption('CONWAYS GAME OF LIFE')
    
    # Paints the screen with the specified color
    glClearColor(grid[0], grid[1], grid[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    screen_size = pygame.display.get_window_size()
    
    cells = zeros((round(screen_size[0]/10),round(screen_size[1]/10)))
    
    rules(cells, 10)
    
    pygame.display.flip()
    
    for point in patterns:
        cells[point[1] // 10,point[0] // 10] = 1
        rules(cells, 10)
        pygame.display.flip()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Game takes life
            running = True
            rules(cells, 10)
                
        glClearColor(grid[0], grid[1], grid[2], 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        
        if running:
            cells = rules(cells, 10, moving=True)
            pygame.display.flip()
        
        time.sleep(0.1)


if __name__ == '__main__':
    main()

