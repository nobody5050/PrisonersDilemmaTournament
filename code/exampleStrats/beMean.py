import numpy
# Reminder: For the history array, "cooperate" = 1, "defect" = 0

def strategy(history, memory):
	choice = "cooperate"
	gameLength = history.shape[1]
	if gameLength > 1:
		if history[1, 1] == 0:
		  choice = "cooperate"
		else:
		  choice = "defect"
	return choice, None
 
	
