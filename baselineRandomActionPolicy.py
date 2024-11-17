#Here we implement the baseline policy/strategy for the snake game


#random actions. 

def randomPolicy(currDir):
    import random

    dirs = {'UP': 0.25, 'DOWN': 0.25, 'LEFT': 0.25, 'RIGHT': 0.25}
    opps = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', "RIGHT": "LEFT"}
    currOpp = opps[currDir]
    validDirections = [d for d in dirs.keys() if d != currOpp]
    return random.choose(validDirections)
