# Модуль для отображения игрового поля
import pygame
from settings import *


class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(10)] for _ in range(20)]
        self.block_size = 25
        self.grid_offset = 50

    def draw_grid(self, screen):
        for y, row in enumerate(self.grid):
            for x, val in enumerate(row):
                pygame.draw.rect(screen, (255, 255, 255), ((x * self.block_size) + self.grid_offset,
                                                           (y * self.block_size) + self.grid_offset,
                                                           self.block_size, self.block_size), 1)

    def update(self):
        pass
