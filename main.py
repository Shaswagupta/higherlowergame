import time
from database import data
import random
from logo import logoo
from logo import vsss
for char in logoo:
    print(char, end="", flush=True)
    time.sleep(0.003)
def randommm():
    choise = random.choice(data)
    print( choise["name"])
    print(f"description : {choise["description"]}")
    print(f"country : {choise["country"]}")

print(" Detailes of  first Person:")
first_person = randommm()
print("\n")
operation1 = first_person 

print(vsss)
print(" Detailes of  second Person:")
second_person = randommm()
operation2 = second_person
userChoise = input("guess who have more follower on instagram 'A' for group A ,'B' for group B ").lower
should = True
point = 0
# while should :
if userChoise == "a":
        if operation1["follower_count"] > operation2["follower_count"]:
            print(f"you are the clear winner \n   follower_count : {operation1["follower_count"]}")
            point += 1

        else :
            print("Oops!! you lost the match ")
elif userChoise == "b":
        if operation1["follower_count"] < operation2["follower_count"]:
            print(f"you are the clear winner \n   follower_count : {operation2["follower_count"]}")
            point += 1

        else :
            print("Oops!! you lost the match ")
else :
        print("what are you doing bro \n yhaa bhiii  mistake!!")