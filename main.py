from game_engine import Game_engine

# TODO: Create a simple logger that logs important points in the game loop and says where it was done

G = Game_engine("card_data2.txt")


G.run_setup()
G.print_player_decks()
G.print_player_hands()
G.print_player_lanes()