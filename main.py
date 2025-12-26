import time
from database import data
import random
from logo import logoo
from logo import vsss
for char in logoo:
    print(char, end="", flush=True)
    time.sleep(0.0015)
def randommm():
    choise = random.choice(data)
    print( choise["name"])
    print(f"description : {choise["description"]}")
    print(f"country : {choise["country"]}")
    return choise

print(" Detailes of  first Person:")
first_person = randommm()
print("\n")
operation1 = first_person 
should = True   
point = 0
while should :
    if point >= 1:
        print(first_person)
    print(vsss)
    print(" Detailes of  second Person:")
    second_person = randommm()
    operation2 = second_person
    userChoise = input("guess who have more follower on instagram 'A' for group A ,'B' for group B..\n.  ")
    abc = first_person["follower_count"]
    cba = second_person["follower_count"]
    
    if userChoise == "A":
        if  abc > cba:
            print(f"you are the clear winner  \n   follower_count : {operation1["follower_count"]}")
            point += 1
        else :
            print("Oops!! you lost the match ")
            restart()
    elif userChoise == "B":
        if abc > cba:
            print(f"you are the clear winner \n   follower_count : {operation2["follower_count"]}")
            point += 1

        else :
            
            print("Oops!! you lost the match ")
            restart()
            
    else :
        print("what are you doing bro \n yhaa bhiii  mistake!!")
def restart():
        restart = input("Do you want to start a new game? (y/n): ").lower()
        if restart == "y":
            print("\nStarting New Game...\n")
            point = 0
            first_person = randommm()
            play_game = True
            while play_game:
                print(vsss)
                print(" Detailes of  second Person:")
                second_person = randommm()
                userChoise = input("guess who have more follower on instagram 'A' for group A ,'B' for group B..\n.  ")
                if userChoise == "A" and abc > cba:
                    print("You won this round!")
                    point += 1
                    first_person = second_person
                else:
                    print("Game Over!")
                    play_game = False
        else:
            print("Thanks for playing!")