import random, numpy as np

# defect = 0, cooperate = 1

"""
hello, this is natura.py
original author is Josh#6441 on discord
this script is completely free to use and modify,
anyone may submit this strat to any tournament,
just dont change the name too drastically,
and give credit where relevant,
please.

hello! Modifications by nobody6502 below:

1. Some of the logic has been changed out for stuff from omega,
2. Round 0 defect, rather than cooperate
3. ftft detection and advantage
4. Joss detection
"""

### https://discord.gg/UFswwahUYu <- discord for all of the smart people who made the winning strategies ###

def DetectJoss(historyNonList, window,):
	AlignMe1 = historyNonList[0, -window:]
	AlignEnemy1 = historyNonList[1, -window - 1:-1]
	
	AlignMe2 = historyNonList[0, -window - 1:-1]
	AlignEnemy2 = historyNonList[1, -window:]
	
	if np.count_nonzero(np.absolute(AlignMe1 - AlignEnemy1) == 1) < np.floor(window / 3) or \
	np.count_nonzero(np.absolute(AlignMe2 - AlignEnemy2) == 1) < np.floor(window / 3):
		# Oof, it's TFT/Joss
		return True
	
	return False

def strategy(history, memory):
    turn = history.shape[1]

    # i like working with lists going forwards
    # instead of arrays going backwards
    opponentMoves = history[1] # different from oppMoves I swear
    historyNonList = history
    num_rounds = history.shape[1]
    
    history = history.tolist()
    ourMoves = history[0][::-1]
    oppMoves = history[1][::-1]
    
    # memory[0]: deadlock counter
    # memory[1]: exploiter counter
    # memory[2]: # of backlogged Cooperations
    # memory[3]: opponent non-blockade Coops
    # memory[4]: non-blockade rounds
    # memory[5]: opponent blockade Coops
    # memory[6]: blockade rounds
    # memory[7]: "isBlockade" boolean
    
    if memory == None:
    	memory = [0,0,0,0,0,0,0,False]
    	choice = "defect"
    	# return choice, memory (temporarily disabled)

    # optimism
    choice = "cooperate"

    # simple start
    if turn == 0:
        return "cooperate", memory

    # not exactly rocket science here either
    if oppMoves[0] == 0: #if defecting
        choice = "defect"

    # very simple de-looper
    if sum(ourMoves[0:6]) + sum(oppMoves[0:6]) < 2: 
        choice = "cooperate"

    # if opponent has never cooperated, then always defect
    if sum(oppMoves) == 0:
        choice = "defect"
    
    # random detection, has to specifically exclude alternating strats
    if turn > 10 and abs(0.5-(sum(oppMoves) / turn )) < 0.1:
        if not ( oppMoves[0:6] == [0,1,0,1,0,1] or oppMoves[0:6] == [1,0,1,0,1,0] ):
            choice = "cooperate"
        
    # simple de-bouncer
    if turn > 6 and ourMoves[0:6] == [1,0,1,0,1,0] and oppMoves[0:6] == [0,1,0,1,0,1]:
        choice = "defect"
        
    # ftft detection
    if len(opponentMoves) > 4:
    	if opponentMoves[2] == 1 and opponentMoves[3] == 0:
    		our_last_move = historyNonList[0, -1] if num_rounds > 0 else 1
    		choice = 0 if our_last_move else 1
			
    # joss detector
    # yeah theres no joss detector. whoops
    if historyNonList.shape[1] > 8 and DetectJoss(historyNonList, 8):
    	choice = "cooperate"
    
    return choice, memory