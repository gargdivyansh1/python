## checking if a number is greatere then a highscore of a game or not 

# create a file of highscore 
with open("Highscore.txt","w") as f:
    f.write("89")
    f.close()

# now make your game like stuff
# first we have to take the random variable which we are checking

import random

def game():
    print("You are playing a game..")
    score = random.randint(1,60) ## this will take input of random numbers from 1 and 60

    ## now we have to fetch the value which we want to check
    with open("Highscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0 

        print(f"Your score {score}")
        if(score>highscore):
            with open("Highscore.txt","w") as f:
                f.write(str(score))
            return score
        else :
            print("Your score is not greater then the highestScore!!")

game()