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
        else:
            print("Invalid input, please enter again")
            murderer_guessed = False

##########

for room in evil.rooms:
    print(room)
guess_room = input("What room was the body in?  ")

for weapon in evil.weapon:
    print(weapon)
guess_weapon = input("What weapon was used?  ")

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
    print(f"Julius was killed with {evil.murder_weapon}.")
    print("+10 points")
else:
    print(f"Julius was killed with {evil.murder_weapon}.")
    print("+0 points")

print(f"Your final score: {points} points")