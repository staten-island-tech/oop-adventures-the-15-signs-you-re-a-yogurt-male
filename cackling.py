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
       

def d_setup(num):
    for index, option in enumerate(dialogues[num]["qs"]):
        print(index,":", option)
def response(char, resp):
    print(evil.char_dialogues[char][resp])
def irritate(char, amount):
    if amount == 5:
        evil.chars[char]["s_irritate"]
    elif amount == 10:
        evil.chars[char]["m_irritate"]
    elif amount == 15:
        evil.chars[char]["l_irritate"]

#How have you been holding up?
def initial_1(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                         #It sure is unfortunate that Julius has died...
        response(char, "unfortunate_1")
        d_setup(5)
        unfortunate(char)
        char.display_name()
    elif select == 1:                                         #Hey so. Did you kill Julius
        response(char, "initial_3")
        d_setup(3)
        initial_3(char)
    elif select == 2:                                         #Have you seen anything unusual lately perhaps?
        response(char, "initial_2")
        d_setup(2)  
        initial_2(char)
    elif select == 3:                                         #[Search character]
        response(char, "initial_4")
        d_setup(4)
        initial_4(char)
    else:
        print("\nDialogue option does not exist. Please choose again")
        initial_1(char)

#Have you seen anything lately
def initial_2(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                         #Okay, thank you!
        response(char, "thanks")
    elif select == 1:                                         #Goodbye
        response(char, "goodbye")
    elif select == 2:                                         #[search character]
        response(char, "initial_4")
        d_setup(4)
        initial_4(char)
    else:
        print("\nDialogue option does not exist. Please choose again")
        initial_2(char)

#are you the one who killed julius
def initial_3(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                         #well who did then?
        response(char, "initial_2")
        d_setup(2)
        initial_2(char)
    elif select == 1:                                         #Okay. Have you seen anything?
        response(char, "initial_2")
        d_setup(2)
        initial_2(char)
    elif select == 2:                                         #I don't believe you
        response(char, "no")
        d_setup(6)
        accusation(char)
    elif select == 3:                                         #Goodbye
        response(char, "goodbye")
    else:
        print("\nDialogue option does not exist. Please choose again")
        initial_3(char)

#search char
def initial_4(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                         #yes
        response(char, "search")
    elif select == 1:                                       #no
        response(char, "thanks")
    else:
        print("\nDialogue option does not exist. Please choose again")
        initial_4(char)

#it sure is unfortunate that julius has died...
def unfortunate(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                         #Have you seen anything unusual lately perhaps?
        response(char, "initial_2")
        d_setup(2)
        initial_2(char)
    elif select == 1:                                         #Hey so. Did you kill Julius
        response(char, "initial_3")
        d_setup(3)
        initial_3(char)
    elif select == 2:                                         #Goodbye
        response(char, "goodbye")
    elif select == 3:                                         #[search character]
        response (char, "search")
        d_setup(4)
        initial_4(char)
    else:
        print("\nDialogue option does not exist. Please choose again")
        unfortunate(char)

#i don't believe you
def accusation(char):
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                           #>:[
        response(char, "no")
        d_setup(6)
        accusation(char)
    elif select == 1:                                         #goodbye
        response(char, "goodbye")
    elif select == 2:                                         #[search character]
        response(char, "initial_4")
        d_setup(4)
        initial_4(char)
    else:
        print("\nDialogue option does not exist. Please choose again")
        accusation(char)

#intro
def qround_1(char):
    response(char, "intro")
    d_setup(0)
    select = int(input("Select a dialogue option:  "))
    if select == 0:                                         # How have you been holding up?
        response(char, "initial_1")
        d_setup(1)
        initial_1(char)
    elif select == 1:                                       #Hey! Have you seen anything lately?
        response(char, "initial_2")
        d_setup(2)
        initial_2(char)
    elif select == 2:                                       #Are you the one who killed Julius??
        response(char, "initial_3")
        d_setup(3)
        initial_3(char)
    elif select == 3:                                       #[search character]
        response(char, "initial_4")
        d_setup(4)
        initial_4(char)
    else:
        print("\nDialogue option does not exist. Please choose again")
        qround_1(char)


def interact(character):
    interacting = "none"
    while evil.chars[character]["anger"] < 40:
        print(evil.chars[character]["anger"])
        qround_1(character)

for index, char in enumerate(evil.chars):
    print(index,":", char["name"])
ask = int(input("Who would you like to interact with?  "))
interact(ask) 

