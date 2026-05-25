import evil

dialogues = [
    {"q" : "initial",
     "qs": ["How have you been holding up?",
            "Hey! Have you seen anything lately?",
            "Are you the one who killed Julius??",
            "[search character]"]},
    #How have you been holding up?
    {"q" :"initial_1" ,
     "qs": ["It sure is unfortunate that Julius has died...",
            "Hey so. Did you kill Julius",
            "Have you seen anything unusual lately perhaps?",
            "[Search character]"]},
    #Hey! Have you seen anything lately?
    {"q" :"initial_2" ,
     "qs": ["Okay, thank you!",
            "Goodbye",
            "[search character]"]},
    #Are you the one who killed Julius??
    {"q" :"initial_3" ,
     "qs": ["Well who did then?", 
            "Okay. Have you seen anything?",
            "I don't believe you", 
            "Goodbye",]},
    #[Search character]
    {"q" :"initial_4" ,
     "qs": ["Yes", "No"]},

    #It sure is unfortunate that Julius has died
    {"q" :"unfortunate_1" ,
     "qs": ["Have you seen anything unusual lately perhaps?", 
            "Hey so. Did you kill Julius", 
            "Goodbye", 
            "[search character]"]},
    #I don't believe you
    {"q" : "accusation_1" ,
     "qs": [">:(", 
            "Goodbye",
            "[search character]"]}
]

c_dialogues = [
    {"name": "Jonathan Sims",
     "intro": "\n15 March, undisclosed year, regarding the death of Julius Caesar. \nStatement begins...\n"
         "It is not often that I find myself facing the murder of a classmate within a school building,\n-----",
     "initial_1" : "\nI am fine, but it does not seem that everyone else appears to be as well.\n-----",
     "initial_2" : "You certainly have some nerve to interrupt an archival recording.\n"
         "I do believe I may have seen {person} carrying {weapon} around... and there was a strange sound coming "
         "from {room} as well, but I cannot be sure.",
     "initial_3" : "Excuse me? What makes you think I would do such a thing as to *murder* a peer of mine, however much I may dislike them?",
     "initial_4" : "Are you sure you want to search this character? You will gain no useful information from this action.",
     "unfortunate_1": "Indeed.",
     "thanks" : "[watches you leave]",
     "goodbye" : "Good riddance. please do not return."
     }
]             

def d_setup(num):
    for index, option in enumerate(dialogues[num]["qs"]):
        print(index,":", option)
def response(char, resp):
    print(c_dialogues[char][resp])

def initial_1(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:
        response(char, "unfortunate_1")
        d_setup(5)
    if select == 1:
        response(char, "initial_3")
        d_setup(3)
    if select == 2:
        response(char, "initial_2")
        d_setup(2)
    if select == 3:
        response(char, "initial_4")
        d_setup(3)

def initial_2(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:
        response(char, "thanks")
    if select == 1:
        response(char, "goodbye")
    if select == 2:
        response(char, "initial_2")
        d_setup(4)

def qround_1(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:
        response(char, "initial_1")
        d_setup(1)
        initial_1(char)
    elif select == 1:
        response(char, "initial_2")
        d_setup(2)

    elif select == 2:
        response(char, "initial_3")
        d_setup(3)

    elif select == 3:
        response(char, "initial_4")
        d_setup(4)

    else:
        print("Dialogue option does not exist. Please choose again")

def interact(character):
    response(character, "intro")
    d_setup(0)
    qround_1(character)

interact(0)