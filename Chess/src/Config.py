import pygame
import os

from Sound import Sound
from Theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self.add_themes()
        self.index = 0
        self.theme = self.themes[self.index]

        self.move_sound = Sound(
            os.path.join('Chess/src/assets/everything_else/move.wav')
        )
        self.capture_sound = Sound(
            os.path.join('Chess/src/assets/everything_else/capture.wav')
        )
        self.theme_change = Sound(
            os.path.join('Chess/src/assets/everything_else/theme_change.wav')
        )

    def change_theme(self):
        self.index += 1
        self.index %= len(self.themes)
        self.theme = self.themes[self.index]

    def add_themes(self):
        default = Theme((210, 210, 210), (90, 90, 90), (244, 247, 116), (172, 195, 51), '#70ff8b', '#008000')
        green = Theme((234, 235, 200), (119, 154, 88), (244, 247, 116), (172, 195, 51), '#C86464', '#C84646')
        brown = Theme((235, 209, 166), (165, 117, 80), (245, 234, 100), (209, 185, 59), '#70ff8b', '#008000')
        blue = Theme((229, 228, 200), (60, 95, 135), (123, 187, 227), (43, 119, 191), '#70ff8b', '#008000')
        gray = Theme((120, 119, 118), (86, 85, 84), (99, 126, 143), (82, 102, 128), '#70ff8b', '#008000')

        self.themes = [default, green, brown, blue, gray]