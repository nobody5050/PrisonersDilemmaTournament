# Tat For Tit just does the oposite of what the previous oponent has done
# Reminder: For the history array, "cooperate" = 1, "defect" = 0

def strategy(history, memory):
    choice = "defect"
    if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to cooperate if and only if the opponent just defected.
        choice = "cooperate"
    return choice, None
