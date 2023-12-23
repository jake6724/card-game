from game_engine import Game_engine
import time
import os
import random

# TODO: Create a simple logger that logs important points in the game loop and says where it was done

G = Game_engine("card_data_sets/card_data4.txt")

G.run_setup()
G.run_game_loop()




# class T:
#     def __init__(self, priority):
#         self.priority = priority
    
#     def __str__(self):
#         return f"T w/ p:{self.priority}"
    
#     def __repr__(self):
#         return f"{self.priority}"

# priorities = ["1", "2", "3", "4"]
# round = 1
# counter = 0

# t_list = []

# for i in range(50):
#     if counter >= 4:
#         counter = 0
#     pv = str(round) + str(priorities[counter])
#     new_t = T(int(pv))
#     counter += 1 
#     round += 1
#     t_list.append(new_t)

# def getp(obj):
#     return obj.priority

# print("Original List:")
# print(t_list)

# print("Shuffled List:")
# random.shuffle(t_list)
# print(t_list)

# print("Resorted List:")
# t_list.sort(key= getp)
# print(t_list)




