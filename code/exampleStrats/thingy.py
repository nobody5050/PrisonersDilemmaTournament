import random

def strategy(history, memory):
	gameLength = history.shape[1]
	if gameLength < 50:
		choice = "cooperate"
		if history.shape[1] >= 2 and history[1,-1] == 0 and history[1,-2] == 0:
			choice = "defect"
			return choice, None
	else:
		return "defect", None