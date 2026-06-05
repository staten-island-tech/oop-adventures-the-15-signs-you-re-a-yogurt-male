
import random
Murderedrooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium" ]
character_list = ["fulgrim", "house","whalen", "jon","wizard","kevin","cecil","sydney"]
global Body_Room
global Murderer
global days
Body_Room = random.choice(Murderedrooms_list)
Murderer = random.choice(character_list)
days = 3 


yaona = ["Yes", "No"]

def inspectjuli():
     if Body_Room == roomwithin:
        print("Julius is in this room. Do you wish to look closer?")
        for index, option in enumerate(yaona):
            print(index, ":", option)
        choice = int(input("Enter the corresponding integer:"))
        if choice == 0:
         print("You step over to where she lies.")
        else:
         print("Whether it be from confusion, fear, disgust, or indifference, you avert your eyes.")
         