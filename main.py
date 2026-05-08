# hallway goal: select list of names.. ect

def movethru():
    required_talk = 1 
    required_walk = 2
    comptalk = 0
    compwalk = 0 
    print("IF you were at home, you'd probably procrastinate getting up-- it is summer break, after all.")
    print("You're, instead, locked in a building with a dead body and 8 potential murderers, so.. It's not exactly easy to rest.")
    print("You walk out into the hallway. Nobody is here, and the windows are still blurred with rain.")
    rooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium", "Back to the broom closet, to sleep."]
    for index, x in enumerate(rooms_list):
            print(index, ":", x)
    chosen_room = int(input("Where would you like to go next? Enter the number corresponding:"))
    print(rooms_list[chosen_room])
    if comptalk or 
movethru()