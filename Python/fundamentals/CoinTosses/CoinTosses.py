import random

def coin_toss(numTosses):
    coin = ["head", "tail"]
    tosses = {coin[0]: 0, coin[1]: 0}

    for toss in range(1, numTosses + 1):
        coinToss = random.randint(0, 1)
        tosses[coin[coinToss]] += 1
        print "Attempt #{0}: Throwing a coin... It's a {1}! ... Got {2} heads(s) so far and {3} tail(s) so far".format(toss, coin[coinToss], tosses['head'], tosses['tail'])

print "Starting the program..."
coin_toss(5000)
print "Ending the program, thank you!"