from random import randint
ans = ""
i = input('rock paper scissors. What Do You Want To Play:')
j = randint(0, 2)
print(j)
if(j == 0):
    ans = "rock"
if(j == 1):
    ans = "paper"
if(j == 2):
    ans = "scissors"

if(i == "rock" and j == 1):
    print(ans)
    print("You lost")

if(i == "rock" and j == 2):
    print(ans)
    print("You Won")

if(i == "rock" and j == 0):
    print(ans)
    print("Draw")

if(i == "paper" and j == 1):
    print(ans)
    print("Draw")

if(i == "paper" and j == 2):
    print(ans)
    print("You lost")

if(i == "paper" and j == 0):
    print(ans)
    print("You Won")

if(i == "Scissor" and j == 1):
    print(ans)
    print("You Won")

if(i == "Scissor" and j == 2):
    print(ans)
    print("Draw")

if(i == "Scissor" and j == 0):
    print(ans)
    print("You lose ")

if(i == "SANJAYISAGOD" and j == 1):
    print(ans)
    print("Found The Easter Egg Eh")


if(i == "SANJAYISAGOD" and j == 2):
    print(ans)
    print("Found The Easter Egg Eh")


if(i == "SANJAYISAGOD" and j == 0):
    print(ans)
    print("Found The Easter Egg Eh")
