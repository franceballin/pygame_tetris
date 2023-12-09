# Главный файл для запуска игры
import pygame
from settings import *
from game import Game
from board import Board
from input_handler import InputHandler

# Инициализация Pygame и создание окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris 2077")

# Создание объектов игры и обработчика ввода
game = Game()
board = Board()
input_handler = InputHandler()

# Основной игровой цикл
running = True
while running:
    input_handler.check_events()
    input_handler.handle_input()

    game.update()  # обновление состояния игры

    screen.fill((0, 0, 0))
    board.draw_grid(screen)

    pygame.display.flip()

pygame.quit()
