import noise
import pygame
import numpy as np

width = 2


def generate_perlin_noise(width, height, scale):
    world = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            world[i][j] = noise.pnoise2(i/scale,
                                        j/scale,
                                        octaves=5,
                                        persistence=0.1,
                                        lacunarity=2.0,
                                        repeatx=200,
                                        repeaty=200,
                                        base=100)
    return world


def map_value(value, from_low, from_high, to_low, to_high):
    """
    Map a value from one range to another.

    :param value: The value to be mapped.
    :param from_low: The minimum value of the original range.
    :param from_high: The maximum value of the original range.
    :param to_low: The minimum value of the target range.
    :param to_high: The maximum value of the target range.
    :return: The mapped value.
    """
    if value < from_high and value < from_low:
        value = from_high
    if value > from_high and value > from_low:
        value = from_high
    if value < from_low and value < from_high:
        value = from_low
    if value > from_low and value > from_high:
        value = from_low
    from_range = from_high - from_low
    to_range = to_high - to_low

    scaled_value = float(value - from_low) / float(from_range)

    return to_low + (scaled_value * to_range)


def clip(value):
    return max(0, value)


def decimal_to_binary(first: int, second: int, third: int, fourth: int):
    return first*8 + second*4 + third*2 + fourth*1


def line(begin: pygame.Vector2, end: pygame.Vector2, screen):
    pygame.draw.line(screen, pygame.Color("White"), begin, end, width)
