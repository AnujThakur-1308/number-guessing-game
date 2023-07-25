###project 1
import random
guess=random.randint(1,100)
for i in range(0,6):
    num=int(input("enter your number"))
    if num<guess:
        print("it is low ")
    elif  num>guess:
        print("it is to high")
    elif num==guess:
        print("wow congo you win")
        break
else:
    print("game over!\nTry again Later  - correct no is",guess)


def msg():
    print("Hello")    