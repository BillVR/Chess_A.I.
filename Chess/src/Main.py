
import sys
import pygame
from Piece import *

from Constants import *
from Game import Game
from Square import *
from Move import Move

class Main:

    # Creando la pantalla
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Chess")
        self.game = Game()

    # Evaluando que el juego esté en ejecución
    def loop(self):

        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_background(self.screen)
            game.show_last_move(self.screen)
            game.show_moves(self.screen)
            game.show_pieces(self.screen)
            game.show_hover(self.screen)

            if dragger.dragging == True:
                dragger.update_blit(self.screen)
                
            if dragger.dragging:
                dragger.update_blit(self.screen)

            for event in pygame.event.get():

                # Click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // square_size # Filas == Y axis
                    clicked_col = dragger.mouseX // square_size # Columnas == X axis

                    # Preguntar si el cuadrado seleccionado tiene una pieza para poder mover
                    if board.squares[clicked_row][clicked_col].has_piece():
                        self.piece = board.squares[clicked_row][clicked_col].piece

                        if self.piece.color == game.next_player:
                            board.calculate_moves(self.piece, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(self.piece)

                            game.show_background(self.screen)
                            game.show_last_move(self.screen)
                            game.show_moves(self.screen)
                            game.show_pieces(self.screen)

                # Arrastrar el mouse
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // square_size
                    motion_col = event.pos[0] // square_size

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_background(self.screen)
                        game.show_last_move(self.screen)
                        game.show_moves(self.screen)
                        game.show_pieces(self.screen)
                        dragger.update_blit(self.screen)

                # Levantar el click del mouse
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // square_size
                        released_col = dragger.mouseX // square_size

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)
                            board.set_true_en_passant(dragger.piece)
                            game.play_sound(captured)
                            game.show_background(self.screen)
                            game.show_pieces(self.screen)
                            game.next_turn()

                    dragger.undrag_piece()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_t:
                        game.change_theme()

                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger


                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                                  
            pygame.display.update()

main = Main()
main.loop()
