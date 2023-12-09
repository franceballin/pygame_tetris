# Главный файл для запуска игры
import pygame
from settings import *
from game import Game
from board import Board
from blocks import Shape
from input_handler import InputHandler

# Инициализация Pygame и создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris 2077")

# Создание объектов игры и обработчика ввода
game = Game()
board = Board()
input_handler = InputHandler()
shape = Shape(100, 50)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)

    input_handler.check_events()
    move_left, move_right, move_down = input_handler.handle_input()

    if move_left:
        shape.move(-1)
    elif move_right:
        shape.move(1)
    elif move_down:
        shape.move_down()
    shape.update()

    screen.fill((0, 0, 0))
    board.draw_grid(screen)
    shape.draw(screen, 25)

    pygame.display.flip()

pygame.quit()
