import random

'''
 Play 10 rounds with a random patern and monitor what
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
	gameLength = history.shape[1]
	if gameLength < 10:
		# print("hi")
		return "cooperate", None
	else:
		return "defect", None
		# TODO implement logic in comment above
	