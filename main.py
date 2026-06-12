# welcome 
import random
from sinister import enterroom
from sinister import makeanaction
from finish import run_end
# first murderer EVER gener  ed: mr. whalen 
Murderedrooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium" ]
character_list = ["fulgrim", "house","whalen", "jon","wizard","kevin","cecil","sydney"]
global Body_Room
global Murderer
global days
Body_Room = random.choice(Murderedrooms_list)
Murderer = random.choice(character_list)
days = 3 

def initialize():

    intro_writing = ["You awake from your shallow rest with a start. ",
    "It took a few moments for you to realize where you were: you're not used to sleeping in a supply closet.",
    "To be fair, you weren’t meant to be in a supply closet at all. You barricaded yourself in here so you could rest safely.",
     "March 13th marked start date of the Discovery program-- Staten Island Tech’s Discovery program-- ",
     "and that day, you and 9 of your peers were to study in order to claim one of their additional seats.",
     "~~~~",
    "All was well until the second day of the program, and a tumultuous summer storm arrived.",
    "Initially, only two of your teachers had called out, but now all of them were gone.",
    "You were supposed to have been left with a sub, but they hightailed it as soon as the streets began to flood.", 
    "It was frightening to be without guidance in a crisis, but atleast you were safe in here! You remembered thinking. ",
    "Those thoughts were then proven wrong, when one of your classmates, Julius, was found dead by your peers.",
    "It's up to you, now, to put the story of her murder together within 3 days."
 ]
    for line in intro_writing: 
         print(line)
    if input("Press anything and then the Enter Key to continue: "):
        print("Intro Complete!")
        

def rungame(): 
    initialize()
    print("You awake with a start, lain supine across a cold tile floor.")
    print(" After hours of no communication with those outside the school, everyone, for the most part, took to different rooms to try and wait out the storm.   ")
    global Body_Room
    global days
    global Murderer

    print(Body_Room)
    havetime = True

    daynumb = range(3)
    NUMBDAY = 0 
    while NUMBDAY in range(3): 
        enterroom()
        if makeanaction() == "BEDDED_TIME":
            NUMBDAY += 1 
    print("You have run out of time.. Now, you must use the clues you've gathered to determine who is the murderer.")
    run_end()
rungame()