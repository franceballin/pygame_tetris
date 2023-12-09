# Модуль для обработки пользовательского ввода
import pygame
from blocks import Shape

shape = Shape(100, 0)


class InputHandler:
    def __init__(self):
        self.move_right = False
        self.move_left = False
        self.last_move_time_left = 0
        self.last_move_time_right = 0
        self.move_delay = 125

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                elif event.key == pygame.K_RIGHT:
                    self.move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                elif event.key == pygame.K_RIGHT:
                    self.move_right = False

    def handle_input(self):
        now = pygame.time.get_ticks()

        if self.move_left:
            if now - self.last_move_time_left > self.move_delay:
                self.last_move_time_left = now
                return True, False
        else:
            self.last_move_time_left = 0

        if self.move_right:
            if now - self.last_move_time_right > self.move_delay:
                self.last_move_time_right = now
                return False, True
        else:
            self.last_move_time_right = 0

        return False, False
