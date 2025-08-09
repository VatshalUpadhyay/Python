import random
def game():
    print("You are playing game..")
    score=random.randint(1,102)
    # fetch the value of score
    with open("Hi_score.txt") as f:
        Hi_score=f.read()
        if(Hi_score!=""):
            Hi_score=int(Hi_score)
        else:
            Hi_score = 0
    print(f"Your score:{score}")
    if(score>Hi_score):
        with open("Hi_score.txt","w")as f:
            f.write(str(score))

    return score

game()