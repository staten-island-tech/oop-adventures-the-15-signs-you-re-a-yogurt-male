import evil

points = 0


for char in evil.chars:
    print(char["name"])

murderer_guessed = False
while murderer_guessed == False:
    guess_char = input("Who is the murderer?  ")
    for char in evil.chars:
        if guess_char == char["name"]:
            murderer_guessed = True
    if murderer_guessed == False:
        print("Invalid input, please enter again")

##########

for room in evil.rooms:
    print(room)

room_guessed = False
while room_guessed == False:
    guess_room = input("What room was the body in?  ")
    for room in evil.rooms:
        if guess_room == room:
            room_guessed = True
    if room_guessed == False:
        print("Invalid input, please enter again")
##########

for weapon in evil.weapon:
    print(weapon)

weapon_guessed = False
while weapon_guessed == False:
    guess_weapon = input("What weapon was used?  ")
    for weapon in evil.weapon:
        if guess_weapon == weapon:
            weapon_guessed = True
    if weapon_guessed == False:
        print("Invalid input, please enter again")
##########

if guess_char == evil.murderer:
    points += 10
    print(f"The murderer was {evil.murderer}.")
    print("+10 points")
else:
    print(f"The murderer was {evil.murderer}.")
    print("+0 points")
if guess_room == evil.murder_room:
    points += 10
    print(f"The body was in {evil.murder_room}.")
    print("+10 points")
else:
    print(f"The body was in {evil.murder_room}.")
    print("+0 points")
if guess_weapon == evil.murder_weapon:
    points += 10
    print(f"Julius Caesar was killed with {evil.murder_weapon}.")
    print("+10 points")
else:
    print(f"Julius Caesar was killed with {evil.murder_weapon}.")
    print("+0 points")

if points == 30:
    print("You found all the information correctly! +20 bonus points")
    points += 20
elif points == 0:
    print("You did not find a single piece of information correctly.")
    print("Even a rock stolen of sentience that it has never posessed would have been able to guess more successfully than you.")
    print("-1000000 points")
    points -= 1000000

print(f"Your final score: {points} points")