from game_engine import Game_engine
import time
import os

# TODO: Create a simple logger that logs important points in the game loop and says where it was done

G = Game_engine("card_data_sets/card_data3.txt")

G.run_setup()
G.run_game_loop()


