import random

rooms = ["Cafeteria", "Compsci Lab", "Auditorium", "Secret pool on the roof", "Engineering Henriques", "Gym", "Goyco Russian"]
weaponl = ["The bag", "Pallete Knife", "Trombone", "Cafeteria Spoon", "Bag of Bricks", "Scurvy Potion", "Sword", "Wizard's Curse"]
items = ["lint", "spare change", 'a red pen', 'a rat', "a crumpled origami crane", "glitter", "the jawbone", "a wet rock", "common loon"]

class Char:
    def __init__(self, full_name, first_name, room, weapon, anger):
        self.full_name = full_name
        self.first_name = first_name
        self.room = room
        self.weapon = weapon
        self.anger = anger
    def display(self):
        info = (f"Murderer: {self.full_name}\nRoom: {self.room}\nWeapon: {self.weapon}")
        return info
    def display_name(self):
        return self.full_name
    def display_mroom(self):
        return self.room
    def display_mweapon(self):
        return self.weapon
    def irritate(self, val):
        self.anger += val
    def display_anger(self):
        return self.anger
        
    
def weaponn():
    w = random.choice(weaponl)
    weaponl.remove(w)
    return (w)

cecil= Char("Cecil Gershwin Palmer", "Cecil", random.choice(rooms), weaponn(), 0)
fulgrim= Char("Fulgrim", "Fulgrim", random.choice(rooms), weaponn(), 0)
jon= Char("Jonathan Sims", "Jon", random.choice(rooms), weaponn(), 0)
whalen = Char("Mr. Whalen", "Mr. Whalen", random.choice(rooms), weaponn(), 0)
wizard = Char("The Wizards is an Animal", "Wizard", random.choice(rooms), weaponn(), 0)
sydney = Char("Sydney Sargent", "Sydney", random.choice(rooms), weaponn(), 0)
house = Char("Dr. Gregory House", "House", random.choice(rooms), weaponn(), 0)
kevin = Char("The Great and Mighty Kevin", "Kevin", random.choice(rooms), weaponn(), 0)

char_list = [cecil, fulgrim, jon, whalen, wizard, sydney, house, kevin]

chars = [
    {"name": cecil.display_name(),
     "val": cecil.display(),
     "room": cecil.display_mroom(),
     "anger": cecil.display_anger(),
     "codeterm": cecil,},
    {"name": fulgrim.display_name(), 
     "val" : fulgrim.display(),
     "room": fulgrim.display_mroom(),
     "anger": fulgrim.display_anger(),
     "codeterm": fulgrim},
    {"name": jon.display_name(),
     "val" : jon.display(),
     "room": jon.display_mroom(),
     "anger": jon.display_anger(),
     "codeterm": jon},
    {"name":whalen.display_name(),
     "val" : whalen.display(),
     "room": whalen.display_mroom(),
     "anger": whalen.display_anger(),
     "codeterm": whalen},
    {"name":wizard.display_name(),
     "val" : wizard.display(),
     "room": wizard.display_mroom(),
     "anger": wizard.display_anger(),
     "codeterm": wizard},
    {"name":sydney.display_name(),
     "val" : sydney.display(),
     "room": sydney.display_mroom(),
     "anger": sydney.display_anger(),
     "codeterm": sydney},
    {"name":house.display_name(),
     "val" : house.display(),
     "room": house.display_mroom(),
     "anger": house.display_anger(),
     "codeterm": house},
    {"name":kevin.display_name(),
     "val" : kevin.display(),
     "room": kevin.display_mroom(),
     "anger": kevin.display_anger(),
     "codeterm": kevin}
]

weapon = ["The bag", "Pallete Knife", "Trombone", "Cafeteria Spoon", "Bag of Bricks", "Scurvy Potion", "Sword", "Wizard's Curse"]

count=0
murderer_choose = random.choice(char_list)
while count < 10:
    count+=1
    char_list.append(murderer_choose)
count=0
murderer = murderer_choose.display_name()
murder_room = random.choice(rooms)
while count < 10:
    count+=1
    rooms.append(murder_room)
count=0
murder_weapon = random.choice(weapon)
weapon.append(murder_weapon)
while count < 10:
    count+=1
    weapon.append(murder_weapon)
#print(murder["val"])

def rand_char():
    for character in char_list:
        return character.display_name()

char_dialogues = [
    {"codeterm": cecil,
     "intro": "\nHello there! I see you've heard about the death of our friend, Caesar sure was a good one.\n-----",
     "initial_1" : "\nOh you know, it's standard for a few interns- ahem. Students- not to make it through the testing process :)\n-----",
     "initial_2" : f"\nHave I seen anything? I've seen many a things. \nAh- you mean about Julius.\n{rand_char()} was walking around {random.choice(rooms)} with {random.choice(weapon)} a while ago, but I wouldn't think much of it.\n-----",
     "initial_3" : "\nHah- killed? Julius? What next, you'll be accusing me of purchasing wheat and wheat byproducts? What kind of blasphemy do you think I am?\n----- ",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "\nLike I said, this happens often. I wouldn't be worried.\n-----",
     "no": "\nI'm sure the Nightvale Sheriff's Secret Police will have a lovely word with you.\n----- ",
     ">:[": "\n[chuckles to himself, shakes his head in pity]\n-----",
     "thanks" : "\nNo problem! Have fun uh, finding out what happened!\n-----",
     "goodbye" : "\nI would hate for you to leave so abruptly, but have fun I suppose!\n-----",
     "search": "\nYou demand Cecil Palmer to empty his pockets; while he gladly complies, every surface of his pants seems to have a pocket, and it takes a while for him to go through all of them. "
         f"From his pockets he takes out what seems to be a mobile portable radio broadcasting system, {cecil.display_mweapon()}, and {random.choice(items)}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm": fulgrim, 
     "intro": "",
     "initial_1" : "",
     "initial_2" : "",
     "initial_3" : "",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "",
     "no": "",
     ">:[": "",
     "thanks" : "",
     "goodbye" : "",
     "search": "\nYou demand ______ to empty [their] pockets, which takes quite a while of convincing for [them] to comply. "
         "From [their] pockets [they] take out what seems to be {random.item}, {self.weapon}, and {random_item}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm": jon,
     "intro": "\n15 March, undisclosed year, regarding the death of Julius Caesar. \nStatement begins...\n"
         "It is not often that I find myself facing the murder of a classmate within a school building,\n-----",
     "initial_1" : "\nI am fine, but it does not seem that everyone else appears to be as well.\n-----",
     "initial_2" : "\nYou certainly have some nerve to interrupt an archival recording.\n"
         f"I do believe I may have seen {rand_char()} carrying {random.choice(weapon)} around... and there was a strange sound coming "
         f"from {random.choice(rooms)} as well, but I cannot be sure.\n-----",
     "initial_3" : "\nExcuse me? What makes you think I would do such a thing as to *murder* a peer of mine, however much I may dislike them?\n-----",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "\nIndeed.\n-----",
     "no": "\nWell I'm not sure what to say then, are you satisfied throwing around mindless accusations? Please leave. I do not wish to continue this conversation.\n-----",
     ">:[": "\n[scowls at you, evidently annoyed]\n-----",
     "thanks" : "\n[watches you leave]\n---",
     "goodbye" : "\nGood riddance. please do not return.\n-----",
     "search": "\nYou demand Jonathan Sims to empty his pockets, which takes quite a while of convincing for him to comply. "
         f"From his pockets he takes out what seems to be a human rib, {jon.display_mweapon}, and {random.choice(items)}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm":whalen,
     "intro": "",
     "initial_1" : "",
     "initial_2" : "",
     "initial_3" : "",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "",
     "no": "",
     ">:[": "",
     "thanks" : "",
     "goodbye" : "",
     "search": "\nYou demand ______ to empty [their] pockets, which takes quite a while of convincing for [them] to comply. "
         "From [their] pockets [they] take out what seems to be {random.item}, {self.weapon}, and {random_item}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm": wizard,
      "intro": "\nThe wizard watches you intently, not in a hostile way; but rather, with curiosity and a wisdom that you can only hope to grasp one day.\n-----",
      "initial_1" : "\nThe wizard does not speak, but whether or not it is unable or does not choose to; you do not know.\n-----",
      "initial_2" : f"\nWhile they do not say any words, the Wizard conjures a hazy scene that seems to picture {rand_char()} in {random.choice(rooms)}, and you think you might see a glimpse of {random.choice(weapon)}.",
      "initial_3" : "\nThe Wizard's expression shifts slightly, as if taken aback. You fear you may have angered them.",
      "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
      "unfortunate_1": "\nThey nod, but you are unsure if the gesture is truly directed towards you.\n-----",
      "no": "The wizard does not like your accusations.",
      ">:[": "The wizard's dislike of you grows.",
      "thanks" : "You feel the wizard's gaze on your back as you leave.",
      "goodbye" : "The wizard's glare, though not initially with ill intent, is now accompanies by an acute irritiation that pierces right through you.\n-----",
      "search": "\nYou lift up the wizard's hat, and immediately regret this decision, as you remember in one of your history classes that touching a wizard's hat is the sign of utmost disrespect. "
         f"The wizard undoubtedly despises you now, and under their hat you can see {random.choice(items)}, {wizard.display_mweapon()}, and a mysterious orb. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm":sydney,
     "intro": "\nHey! There seems to be a lot of commotion this morning, right? [awkward chuckle]\n-----",
     "initial_1" : "\nSorry? Is there something that happened?\n-----",
     "initial_2" : f"\nNothing much! Just the rain... falling down... down... and down...\nI also did find {random.choice(weapon)} when looking around {random.choice(rooms)}, right after {rand_char()} walked out!\nNot sure why you'd need to know that, though.\n----- ",
     "initial_3" : "\nShe's dead?? I can't believe this... and you think I'd be the one to kill her?\n",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "Julius is dead?? Caesar? Julius Caesar? Oh I knew those birds would drive us all crazy one day. They've been singing about the Ides of March for as long as I can remember. How unfortunate.\n-----",
     "no": "\nWhy would you think that I would ever kill Julius?? Or anyone, even?\n-----",
     ">:[": "\nI'm- not sure I want to speak to you anymore. Please leave\n-----",
     "thanks" : "\nOf course! I do hope you find who killed Julius, I sure will miss her...\n-----",
     "goodbye" : "\nAnd you're just leaving. Alright. I see. Bye?\n-----",
     "search": "You demand Sydney to empty his pockets, to which he gets very defensive and annoyed. Eventually however, he does. "
         f"From his pockets he takes out a jar of worms, {sydney.display_mweapon()}, and {random.choice(items)}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm":house,
    "intro": "",
     "initial_1" : "",
     "initial_2" : "",
     "initial_3" : "",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "",
     "no": "",
     ">:[": "",
     "thanks" : "",
     "goodbye" : "",
     "search": "\nYou demand ______ to empty [their] pockets, which takes quite a while of convincing for [them] to comply. "
         "From [their] pockets [they] take out what seems to be {random item}, {self weapon}, and {random item}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"codeterm":kevin,
     "intro": "",
     "initial_1" : "",
     "initial_2" : "",
     "initial_3" : "",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "",
     "no": "",
     ">:[": "",
     "thanks" : "",
     "goodbye" : "",
     "search": "\nYou demand ______ to empty [their] pockets, which takes quite a while of convincing for [them] to comply. "
         "From [their] pockets [they] take out what seems to be {random item}, {self weapon}, and {random item}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
]

#print(murderer,"\n",murder_room,"\n",murder_weapon)

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
       

def d_setup(num, char, p_list):
    ch = p_list[char]
    if ch.display_anger() < 20:
        for index, option in enumerate(dialogues[num]["qs"]):
            print(index,":", option)
def response(char, resp, p_list):
    d_list = []
    for dlogs in char_dialogues:
        for term in p_list:
            if dlogs["codeterm"] == term:
                d_list.append(dlogs)
    print(d_list[char][resp])
def iirritate(char, amount, p_list):
    ch = p_list[char]
    ch.irritate(amount)
    print(ch.display_anger())


#How have you been holding up?
def initial_1(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                         #It sure is unfortunate that Julius has died...
            response(char, "unfortunate_1", p_list)
            d_setup(5, char, p_list)
            unfortunate(char, p_list)
        elif select == 1:                                         #Hey so. Did you kill Julius
            iirritate(char, 10)
            response(char, "initial_3", p_list)
            d_setup(3, char, p_list)
            initial_3(char, p_list)
        elif select == 2:                                         #Have you seen anything unusual lately perhaps?
            response(char, "initial_2", p_list)
            d_setup(2, char, p_list)  
            initial_2(char, p_list)
        elif select == 3:                                         #[Search character]
            response(char, "initial_4", p_list)
            d_setup(4, char, p_list)
            initial_4(char, p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            initial_1(char, p_list)

#Have you seen anything lately
def initial_2(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                         #Okay, thank you!
            response(char, "thanks", p_list)
        elif select == 1:                                         #Goodbye
            iirritate(char, 5, p_list)
            response(char, "goodbye", p_list)
        elif select == 2:                                         #[search character]
            response(char, "initial_4", p_list)
            d_setup(4, char, p_list)
            initial_4(char, p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            initial_2(char, p_list)

#are you the one who killed julius
def initial_3(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                         #well who did then?
            response(char, "initial_2", p_list)
            d_setup(2, char, p_list)
            initial_2(char, p_list)
        elif select == 1:                                         #Okay. Have you seen anything?
            response(char, "initial_2", p_list)
            d_setup(2, char, p_list)
            initial_2(char, p_list)
        elif select == 2:                                         #I don't believe you
            iirritate(char, 10, p_list)
            response(char, "no", p_list)
            d_setup(6, char, p_list)
            accusation(char, p_list)
        elif select == 3:                                         #Goodbye
            iirritate(char, 5, p_list)
            response(char, "goodbye", p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            initial_3(char, p_list)

#search char
def initial_4(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                         #yes
            iirritate(char, 15, p_list)
            response(char, "search", p_list)
        elif select == 1:                                       #no
            iirritate(char, 5, p_list)
            response(char, "goodbye", p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            initial_4(char, p_list)

#it sure is unfortunate that julius has died...
def unfortunate(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                         #Have you seen anything unusual lately perhaps?
            response(char, "initial_2", p_list)
            d_setup(2, char, p_list)
            initial_2(char, p_list)
        elif select == 1:                                         #Hey so. Did you kill Julius
            iirritate(char, 10, p_list)
            response(char, "initial_3", p_list)
            d_setup(3, char, p_list)
            initial_3(char, p_list)
        elif select == 2:                                         #Goodbye
            iirritate(char, 5, p_list)
            response(char, "goodbye", p_list)
        elif select == 3:                                         #[search character]
            response (char, "search", p_list)
            d_setup(4, char, p_list)
            initial_4(char, p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            unfortunate(char, p_list)

#i don't believe you
def accusation(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                           #>:[
            iirritate(char, 10, p_list)
            response(char, "no", p_list)
            d_setup(6, char, p_list)
            accusation(char, p_list)
        elif select == 1:                                         #goodbye
            iirritate(char, 5, p_list)
            response(char, "goodbye", p_list)
        elif select == 2:                                         #[search character]
            response(char, "initial_4", p_list)
            d_setup(4, char, p_list)
            initial_4(char, p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            accusation(char, p_list)

#intro
def qround_1(char, p_list):
    ch = p_list[char]
    if ch.display_anger() >= 20:
        print("You have irritated this character past their capacity for tolerance. You can no longer interact with them.")
    else:
        response(char, "intro", p_list)
        d_setup(0, char, p_list)
        select = int(input("Select a dialogue option:  "))
        if select == 0:                                         # How have you been holding up?
            response(char, "initial_1", p_list)
            d_setup(1, char, p_list)
            initial_1(char, p_list)
        elif select == 1:                                       #Hey! Have you seen anything lately?
            response(char, "initial_2", p_list)
            d_setup(2, char, p_list)
            initial_2(char, p_list)
        elif select == 2:                                       #Are you the one who killed Julius??
            iirritate(char, 10, p_list)
            response(char, "initial_3", p_list)
            d_setup(3, char, p_list)
            initial_3(char, p_list)
        elif select == 3:                                       #[search character]
            response(char, "initial_4", p_list)
            d_setup(4, char, p_list)
            initial_4(char, p_list)
        else:
            print("\nDialogue option does not exist. Please choose again")
            qround_1(char, p_list)

interacting = "none"
def interact(character, p_list):
    interacting = p_list[character]
    ch = char_list[character]
    print(ch.display_anger())
    qround_1(character, p_list)
        

""" for index, char in enumerate(chars):
    print(index,":", char["name"])
ask = int(input("Who would you like to interact with?  "))
interact(ask)  """

