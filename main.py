# Snake Water Gun........................
import random

def game(comp,you):
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
    elif you == 'g':
        return True
    elif comp =='w':
        if you == 's':
            return True
        if you =='g':
            return False 
    elif comp =='g':
        if you == 'w':
            return True
        if you =='s':
            return False

print("Comp Turn: Snake(s) Water(w) Gun(g) : ")
rand=random.randint(1,3)
if rand == 1:
    comp ='s'
elif rand == 2:
    comp = 'w' 
elif rand == 3:
    comp = 'g' 

you=input("Player's Turn: Snake(s) Water(w) Gun(g) : ")

result=game(comp,you)

print(f"Computer Chose: {comp}")
print(f"You Chose: {you}")

if result == None:
    print("Game Is Tie,Play Again")

elif result == True:
    print("Congratulation,You Win..")
elif result ==False:
    print("You Lose,Play One More Time")
