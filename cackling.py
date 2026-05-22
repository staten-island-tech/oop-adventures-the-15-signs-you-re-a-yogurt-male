import evil

""" initial = ["How have you been holding up?",
           "Hey! Have you seen anything lately?",
           "Are you the one who killed Julius??",
           "[search character]"]
#How have you been holding up?
initial_1 = ["It sure is unfortunate that Julius has died...",
             "Hey so. Did you kill Julius",
             "Have you seen anything unusual lately perhaps?"
             "[Search character]"]
#Hey! Have you seen anything lately?
initial_2 = ["Okay, thank you!",
             "Goodbye",
             "[search character]"]
#Are you the one who killed Julius??
initial_3 = ["Well who did then?", 
             "Okay. Have you seen anything?",
             "I don't believe you", 
             "Goodbye",
             ""]
#[Search character]
initial_4 = ["Yes", "No"]

#It sure is unfortunate that Julius has died
unfortunate_1 = ["Have you seen anything unusual lately perhaps?", 
             "Okay, thank you!", 
             "Goodbye", 
             "[search character]"]
#I don't believe you
accusation_1 = [">:(", 
                "Goodbye",
                "[search character]"] """

#dictionary version of the lists above
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
            "Have you seen anything unusual lately perhaps?"
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
            "Okay, thank you!", 
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
     "initial_2" : "You certainly have some nerve to interrupt an archival recording. Make it quick-\n"
         "I do believe I may have seen {person} carrying {weapon} around… there was a strange sound coming "
         "from {room} as well but I cannot be sure.",
     "initial_3" : "Excuse me? What makes you think I would do such a thing as to *murder* a peer of mine, however much I may dislike them?",
     "initial_4" : "Are you sure you want to search this character? You will gain no useful information from this action.",
     "unfortunate_1": "I was walking past {room} earlier and did see {person} with {weapon}, but I am unsure.",
     }
]             


def interact(character):
    print(c_dialogues[character]["intro"])
    for index, option in enumerate(dialogues[0]["qs"]):
        print(index,":", option)
    select = int(input("Select a dialogue option:  "))
    if select == 0:
        print(c_dialogues[character]["initial_1"])
        for index, option in enumerate(dialogues[1]["qs"]):
            print(index,":", option)

interact(0)