import pygame
from var import *


def write_text(surf, x, y, text, size, bg_color, color=default_text_color): #(50, 200, 50)
    font = pygame.font.Font('Vocaloid-Bapx.ttf', size)
    text = font.render(text, True, color, bg_color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    surf.blit(text, textRect)