
import pygame
from Constants import *
from Board import Board
from Dragger import Dragger
from Config import Config
from Square import Square

class Game:

    def __init__(self):
        self.next_player = "white"
        self.hovered_square = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    # Creación del tablero por defecto
    def show_background(self, surface):
        theme = self.config.theme

        for row in range(rows):
            for col in range(columns):
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                rectangle = (col * square_size, row * square_size, square_size, square_size)
                pygame.draw.rect(surface, color, rectangle)

    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(columns):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 64)
                        image = pygame.image.load(piece.texture)
                        image_center = col * square_size + square_size // 2, row * square_size + square_size // 2
                        piece.texture_rectangle = image.get_rect(center = image_center)
                        surface.blit(image, piece.texture_rectangle)

    def show_moves(self, surface):
        theme = self.config.theme

        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                color = theme.moves.light if ((move.final.row + move.final.col) % 2 == 0) else theme.moves.dark
                rectangle = (move.final.col * square_size, move.final.row * square_size, square_size, square_size)
                pygame.draw.rect(surface, color, rectangle)

    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                rectangle = (pos.col * square_size, pos.row * square_size, square_size, square_size)
                pygame.draw.rect(surface, color, rectangle)

    def show_hover(self, surface):
        if self.hovered_square:
            color = (255, 255, 255)
            rectangle = (self.hovered_square.col * square_size, self.hovered_square.row * square_size, square_size, square_size)
            pygame.draw.rect(surface, color, rectangle, width = 3)

    def next_turn(self):
        self.next_player = "white" if self.next_player == "black" else "black"

    def set_hover(self, row, col):
        self.hovered_square = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()
        self.config.theme_change.play()

    def play_sound(self, captured = False):
        if captured:
            self.config.capture_sound.play() 
        else:
            self.config.move_sound.play()

    def reset(self):
        self.__init__()