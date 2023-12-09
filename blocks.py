# Модуль для описания блоков (фигур)
import pygame
import random

class Block:
    def __init__(self, color):
        self.color = color

    def draw(self, screen, x, y, block_size):
        pygame.draw.rect(screen, self.color, (x, y, block_size, block_size))

    def update(self):
        pass


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 0)
        self.blocks = self.create_random_shape()
        self.fall_time = pygame.time.get_ticks()
        self.fall_speed = 10
        self.move_speed = 25
        self.last_fall = pygame.time.get_ticks()
        self.fall_interval = 500

    def create_random_shape(self):
        shapes = [
            [[Block(self.color), Block(self.color)],
             [Block(self.color), Block(self.color)]],
        ]
        return random.choice(shapes)

    def draw(self, screen, block_size):
        for row_offset, row in enumerate(self.blocks):
            for col_offset, block in enumerate(row):
                block.draw(screen,
                           (self.x + col_offset * block_size),
                           (self.y + row_offset * block_size),
                           block_size)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_fall >= self.fall_interval:
            self.move_down()
            self.last_fall = now

    def move_down(self):
        self.y += 25

    def move(self, dx):
        self.x += dx * self.move_speed