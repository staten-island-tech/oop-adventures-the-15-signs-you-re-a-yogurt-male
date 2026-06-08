from evil import murder_room
from evil import murder_weapon
# import random
# Murderedrooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium" ]
# character_list = ["fulgrim", "house","whalen", "jon","wizard","kevin","cecil","sydney"]
# global Body_Room
# global Murderer
# global days
# Body_Room = random.choice(Murderedrooms_list)
# Murderer = random.choice(character_list)
# days = 3 



def bodyfacts(): 
    if murder_weapon == "Pallete Knife" or murder_weapon == "Cafeteria Spoon":
        print("They look pale, likely a consequence of being bled dry. There are a few small, rough stab wounds on their torso.")
    elif murder_weapon == "Wizard's Curse":
        print("Julius' body looks unexplainably, arcanely charred, but the room doesn't smell like smoke and the only thing crisp in this room is her.")
    elif murder_weapon == "Trombone" or murder_weapon == "Bag of Bricks":
        print("Julius looks.. fine? Asides from a few bruises and an odd contorted pose, there's no blood anywhere.")
    elif murder_weapon == "The bag":
        print("Parts of Julius are completely missing. Not torn apart, not sawn off. Just gone- like they've been swallowed by a portal.")
    elif murder_weapon == "Sword":
        print("You can see a very clean stab wound through Julius' abdomen, and the blood pooling beneath her suggests whatever made it went all the way through.")
    elif murder_weapon == "Scurvy Potion":
        print("Julius' body, immediately, gives you the impression of decay. You know they were perfectly healthy just a couple days ago, but their bloodied lips and mottled tan and red skin suggest otherwise.")

