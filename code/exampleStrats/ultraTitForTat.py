import random
import numpy

'''
 Play 10 rounds with a set patern and monitor what
 happens, try to dicern from this which strategy they
 are using and then use the best strategy against them
 
 For instance, if they are always cooperating we want to
 always defect, however if they are playing conMan we
 can see that and adjust acordingly
 
 BUT WAIT! Why so many rounds of listening?!
 
 This is done to outsmart strategies like detective and con man,
 both of which will have finished their detecting period before we reach our 10.
 eventually i'd like to convert this to listening the
 whole game and updating its prediction from that but I
 will need to spend more time in the algorithm to do that.
'''

def strategy(history, memory):
	return "cooperate", None
	gameLength = history.shape[1]
	if gameLength == 3 and Trust != False:
		# Since the detective does cooperate defect cooperate cooperate, we can detect this at round 3
		if history[1, -3] == 1 and history[1, -2] == 0 and history[1, -1] == 1:
			# this means the oponent is playing detective.
			detective = True
			return "defect", detective # this will work against round 4 detective, but will set them to tit for tat
		else:
			return "cooperate", None
			# they arent a detective
	else: 
		# return "cooperate", None
		if gameLength == 1:
			if history[1, -1] == 0:
				# they defected in the first turn. never trust them
				Trust = False
				return "defect", trust
		else:
			return "cooperate"
			# neither detective nor defect on first turn