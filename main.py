import math
import sys
import pygame
import numpy
import noise
import functions as func


pygame.init()
size = (800, 800)
flags = pygame.HWSURFACE | pygame.DOUBLEBUF  # Hardware surface and double buffering
screen = pygame.display.set_mode(size, flags)
pygame.display.set_caption("Marching Square Example")
clock = pygame.time.Clock()

resolution = 10

increment = 0.1
time_offset = 0

columns = int(screen.get_width() / resolution)+1
rows = int(screen.get_height() / resolution)+1
field = numpy.zeros((rows, columns))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    # screen.fill((120, 120, 120))
    screen.fill((0, 0, 0))

    # Generate noise surface
    x_offset = 0
    for i in range(rows):
        y_offset = 0
        x_offset += increment
        for j in range(columns):
            field[i][j] = noise.snoise3(x_offset, y_offset, time_offset, persistence=0.1)
            y_offset += increment

    # Update time for surface generation
    time_offset += 0.05

    # # Loop for drawing grid
    # for i in range(rows):
    #     for j in range(columns):
    #         color = pygame.Color(int(func.clip(field[i][j])*255),
    #                              int(func.clip(field[i][j])*255), int(func.clip(field[i][j])*255))
    #         pygame.draw.circle(screen, color, (i*resolution, j*resolution), 5)

    # Loop for calculate the midpoints and draw the border
    for i in range(rows-1):
        for j in range(columns-1):
            x = i * resolution
            y = j * resolution

            a = pygame.Vector2(x + resolution * 0.5, y)
            b = pygame.Vector2(x + resolution,       y + resolution * 0.5)
            c = pygame.Vector2(x + resolution * 0.5, y + resolution)
            d = pygame.Vector2(x,                    y + resolution * 0.5)

            state = func.decimal_to_binary(math.ceil(field[i][j]),
                                           math.ceil(field[i+1][j]),
                                           math.ceil(field[i+1][j+1]),
                                           math.ceil(field[i][j+1]))

            if state == 1:
                func.line(c, d, screen)
            elif state == 2:
                func.line(b, c, screen)
            elif state == 3:
                func.line(b, d, screen)
            elif state == 4:
                func.line(a, b, screen)
            elif state == 5:
                func.line(a, d, screen)
                func.line(b, c, screen)
            elif state == 6:
                func.line(a, c, screen)
            elif state == 7:
                func.line(a, d, screen)
            elif state == 8:
                func.line(a, d, screen)
            elif state == 9:
                func.line(a, c, screen)
            elif state == 10:
                func.line(a, b, screen)
                func.line(c, d, screen)
            elif state == 11:
                func.line(a, b, screen)
            elif state == 12:
                func.line(b, d, screen)
            elif state == 13:
                func.line(b, c, screen)
            elif state == 14:
                func.line(c, d, screen)

    pygame.display.flip()
    clock.tick(60)
