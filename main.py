# welcome 
import random
# first murderer EVER generated: mr. whalen 
Murderedrooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium" ]
character_list = ["fulgrim", "house","whalen", "jon","wizard","kevin","cecil","sydney"]


def initialize():
    Body_Room = random.choice(Murderedrooms_list)
    Murderer = random.choice(character_list)
    print(Murderer)

    intro_writing = ["You awake from your shallow rest with a start. ",
    "It took a few moments for you to realize where you were: you're not used to sleeping in a supply closet.",
    "To be fair, you weren’t meant to be in a supply closet at all. You barricaded yourself in here so you could rest safely.",
     "March 13th marked start date of the Discovery program-- Staten Island Tech’s Discovery program-- ",
     "and that day, you and 6 of your peers were to study in order to claim one of their additional seats.",
     "~~~~",
    "All was well until the second day of the program, and a tumultuous summer storm arrived.",
    "Initially, only two of your teachers had called out, but now all of them were gone.",
    "You were supposed to have been left with a sub, but they hightailed it as soon as the streets began to flood.", 
    "It was frightening to be without guidance in a crisis, but atleast you were safe in here! You remembered thinking. ",
    f"Those thoughts were then proven wrong, when one of your classmates, Julius, was found dead in {Body_Room}.",
 ]
    player_name = input("Welcome! Before the game begins, please state your name: ")
    for line in intro_writing: 
         print(line)
    if input("Type X and press the Enter key to continue: "):
        print("Intro Complete!")
initialize()