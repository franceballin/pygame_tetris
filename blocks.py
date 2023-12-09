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
        self.at_bottom = False

    def create_random_shape(self):
        shapes = [
            [[Block(self.color), Block(self.color)], [Block(self.color), Block(self.color)]]
        ]
        return random.choice(shapes)

    def draw(self, screen, block_size):
        for row_offset, row in enumerate(self.blocks):
            for col_offset, block in enumerate(row):
                if block is not None:
                    block.draw(screen,
                               (self.x + col_offset * block_size),
                               (self.y + row_offset * block_size),
                               block_size)
                else:
                    pass

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_fall >= self.fall_interval:
            if not self.check_collision(0, 1):
                self.move_down()
                self.last_fall = now
            else:
                self.at_bottom = True
                self.create_new_shape()

    def create_new_shape(self):
        self.x = 100
        self.y = 50

        self.blocks = self.create_random_shape()
        self.at_bottom = False

    def move_down(self):
        if not self.check_collision(0, 1):
            self.y += 25

    def move(self, dx):
        if not self.at_bottom:
            new_x = self.x + dx * 25
            if 50 <= new_x < 275 - len(self.blocks[0]) + 1:
                self.x = new_x

    def check_collision(self, dx, dy):
        for row_offset, row in enumerate(self.blocks):
            for col_offset, block in enumerate(row):
                new_x = self.x + col_offset + dx
                new_y = self.y + row_offset + dy
                if new_y >= 500:
                    return True

        return False