from decimal import Decimal
import random

import numpy as np

num_rounds = history.shape[1]
testing_schedule = [1, 0, 0, 1, 1]
max_defection_threshold = Decimal(1) / Decimal(2)  # do not forgive high defections
small_defection_window = 20
max_local_unprovoked_defections = 5  # too many unprovoked defections? random
joss_unprovoked_defections = 2 # in a window of 20, this is equal to 10%. 10% defections is what you should expect from joss

 # Detective, except:
 # - use nprtt instead of tit-for-tat for the forgiveness heuristic
 # - detect random and spam DDDD since defection is optimal with random
 # - detect ftft and spam DCDCDCDCDC to take advantage of it
 # - detect alwaysCooperate and spam DDDDD to take advantage of it, at the cost of the
 #   grimTrigger

def alternate(history, memory):
	our_last_move = history[0, -1] if num_rounds > 0 else 1
	choice = 0 if our_last_move else 1
	memory = "alternate"

def defect(history, memory):
	# break out of defection if they cooperated twice in a row
	last_two_opponent_moves = history[1, -2:]
	if np.count_nonzero(last_two_opponent_moves) == 0:
		choice = 1
		memory = "tit-for-tat"
	else:
		choice = 0
		memory = "defect"

def alwaysDefect(history, memory):
	if history[1, -1] == 0:  # uh oh, we predicted wrong!
	  choice = 0
	  memory = "tit-for-tat"
	else:
		choice = 0
		memory = "alwaysDefect"
	
def strategy(history, memory):
     """
     :history: 2d numpy array of our and opponent past moves
     :memory: mode string, which may be None, 'tit-for-tat', 'alternate', 'defect', or
         'defect_assuming_cooperative'
     """

     if num_rounds < len(testing_schedule):  # intitial testing phase
         choice = testing_schedule[num_rounds]
     elif num_rounds == len(testing_schedule):  # time to transition to our modes
         opponent_moves = history[1]
         opponent_stats = dict(zip(*np.unique(opponent_moves, return_counts=True)))
         if opponent_stats.get(0, 0) < 1:  # they never defected, take advantage of them
             choice = 0
             memory = "alwaysDefect"
         elif opponent_stats.get(0, 0) == len(testing_schedule):  # they always defect
             choice = 0
             memory = "defect"
         elif opponent_moves[2] == 1 and opponent_moves[3] == 0:  # ftft detected
             choice = 0
             memory = "alternate"
         else:
             choice = 1
             memory = "tit-for-tat"
     else:  # num_rounds > len(testing_schedule)
         if memory == "defect":
         	defect(history, memory)
         elif memory == "alwaysDefect":
         	alwaysDefect(history, memory)
         elif memory == "alternate":
             alternate(history, memory)
         else:  # nprtt or None
             # first check whether we've detected a random
             window_start = max(0, num_rounds - small_defection_window)
             window_end = num_rounds
             opponents_recent_moves = history[1, window_start + 1 : window_end]
             our_recent_moves = history[0, window_start : window_end - 1]
             defections = opponents_recent_moves - our_recent_moves
             opponents_recent_defections = np.count_nonzero(defections == 1)
             if opponents_recent_defections > max_local_unprovoked_defections:
                 choice = 0
                 memory = "defect"

             else:
             	WINDOW_SIZE = 5
             	FREE_PASS = 0  # we forgive if they defect during the first FREE_PASS turns
             	
             	num_rounds = history.shape[1]
             	
             	opponents_last_move = history[1, -1] if num_rounds >= 1 else 1
             	our_second_last_move = history[0, -2] if num_rounds >= 2 else 1
             	
             	choice = 1
             	if opponents_last_move == 0:
             		window_start = max(num_rounds - WINDOW_SIZE, 0)
             		window_end = num_rounds
             		opponent_recent_moves = history[1, window_start:window_end]
             		opponent_recent_stats = dict(
             			zip(*numpy.unique(opponent_recent_moves, return_counts=True))
             			)
             	consider_forgiving = False
             	if num_rounds <= FREE_PASS:
             		consider_forgiving = True
             	elif opponent_recent_stats.get(1, 0) > 0:
             		consider_forgiving = True
             	 	
             	 	# only forgive defections if they've cooperated with us in the past 5 rds
             choice = (
             	 		1
             	 		if (
             	 			opponents_last_move == 1
             	 			or (consider_forgiving and our_second_last_move == 0)
             	 			)
             	 		else 0
             	 		)
             memory = "tit-for-tat"

     return choice, memory
