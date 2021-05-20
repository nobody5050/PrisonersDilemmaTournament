import random

def strategy(history, memory):
	gameLength = history.shape[1]
	if gameLength < 50:
		return "defect", None
	else:
		if random.randint(0,1) == 0:
			return "cooperate", None
		else:
			return "defect", None