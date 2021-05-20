# Begrudging Tit for Tat.
# Choose to forgive if and only if the opponent just cooperated TWICE in a row.

# Reminder: For the history array, "cooperate" = 1, "defect" = 0

def strategy(history, memory):
    choice = "defect"
    if history.shape[1] >= 2 and history[1,-1] == 1 and history[1,-2] == 1: # We check the TWO most recent turns to see if BOTH were defections, and only then do we defect too.
        choice = "cooperate"
    return choice, None
