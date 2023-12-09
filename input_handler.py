# Модуль для обработки пользовательского ввода
import pygame

class InputHandler:
    def __init__(self):
        pass

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_DOWN]:
            pass
        elif keys[pygame.K_UP]:
            pass
        elif keys[pygame.K_SPACE]:
            pass