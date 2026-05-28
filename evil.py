import random

rooms = ["Cafeteria", "Compsci Lab", "Auditorium", "Secret pool on the roof", "Engineering Henriques", "Gym", "Goyco Russian"]
weaponl = ["The bag", "Pallete Knife", "Trombone", "Cafeteria Spoon", "Bag of Bricks", "Scurvy Potion", "Sword", "Wizard's Curse"]
items = ["lint", "spare change", 'a red pen', 'a rat', "a crumpled origami crane", "glitter", "the jawbone", "a wet rock", "common loon"]
class char:
    def __init__(self, full_name, first_name, room, weapon):
        self.full_name = full_name
        self.first_name = first_name
        self.room = room
        self.weapon = weapon

    def display(self):
        info = (f"Murderer: {self.full_name}\nRoom: {self.room}\nWeapon: {self.weapon}")
        return info
    def display_name(self):
        return self.full_name
    def display_mroom(self):
        return self.room
    def display_mweapon(self):
        return self.weapon
    
def weaponn():
    w = random.choice(weaponl)
    weaponl.remove(w)
    return (w)

cecil= char("Cecil Gershwin Palmer", "Cecil", random.choice(rooms), weaponn())
fulgrim= char("Fulgrim", "Fulgrim", random.choice(rooms), weaponn())
jon= char("Jonathan Sims", "Jon", random.choice(rooms), weaponn())
whalen = char("Mr. Whalen", "Mr. Whalen", random.choice(rooms), weaponn())
wizard = char("The Wizards is an Animal", "Wizard", random.choice(rooms), weaponn())
sydney = char("Sydney Sargent", "Sydney", random.choice(rooms), weaponn())
house = char("Dr. Gregory House", "House", random.choice(rooms), weaponn())
kevin = char("The Great and Mighty Kevin", "Kevin", random.choice(rooms), weaponn())

chars = [
    {"name": cecil.display_name(),
     "val": cecil.display(),
     "room": cecil.display_mroom(),
     "intro": "\nHello there! I see you've heard about the death of our friend, Caesar sure was a good one.\n-----",
     "initial_1" : "\nOh you know, it's standard for a few interns- ahem. Students- not to make it through the testing process :)\n-----",
     "initial_2" : f"\nHave I seen anything? I've seen many a things. \nAh- you mean about Julius.\n{random.choice(person)} was walking around {room} with {weapon} a while ago, but I wouldn't think much of it.\n-----",
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
    {"name": fulgrim.display_name(), 
     "val" : fulgrim.display(),
     "room": fulgrim.display_mroom(),
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
    {"name": jon.display_name(),
     "val" : jon.display(),
     "room": jon.display_mroom(),
     "intro": "\n15 March, undisclosed year, regarding the death of Julius Caesar. \nStatement begins...\n"
         "It is not often that I find myself facing the murder of a classmate within a school building,\n-----",
     "initial_1" : "\nI am fine, but it does not seem that everyone else appears to be as well.\n-----",
     "initial_2" : "\nYou certainly have some nerve to interrupt an archival recording.\n"
         "I do believe I may have seen {person} carrying {weapon} around... and there was a strange sound coming "
         "from {room} as well, but I cannot be sure.\n-----",
     "initial_3" : "\nExcuse me? What makes you think I would do such a thing as to *murder* a peer of mine, however much I may dislike them?\n-----",
     "initial_4" : "\nAre you sure you want to search this character? You will gain no useful information from this action.\n-----",
     "unfortunate_1": "\nIndeed.\n-----",
     "no": "\nWell I'm not sure what to say then, are you satisfied throwing around mindless accusations? Please leave. I do not wish to continue this conversation.\n-----",
     ">:[": "\n[scowls at you, evidently annoyed]\n-----",
     "thanks" : "\n[watches you leave]\n---",
     "goodbye" : "\nGood riddance. please do not return.\n-----",
     "search": "\nYou demand Jonathan Sims to empty his pockets, which takes quite a while of convincing for him to comply. "
         "From his pockets he takes out what seems to be a human rib, {self.weapon}, and {random_item}. "
         "\nThese things are of no use to you, for the weapon could have been anyone's and the other items are harmless. \n-----"},
    {"name":whalen.display_name(),
     "val" : whalen.display(),
     "room": whalen.display_mroom(),
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
    {"name":wizard.display_name(),
     "val" : wizard.display(),
     "room": wizard.display_mroom(),
     "intro": "\nThe wizard watches you intently, not in a hostile way; but rather, with curiosity and a wisdom that you can only hope to grasp one day.\n-----",
     "initial_1" : "\nThe wizard does not speak, but whether or not it is unable or does not choose to; you do not know.\n-----",
     "initial_2" : "\nWhile they do not say any words, the Wizard conjures a hazy scene that seems to picture {person} in {room}, and you think you might see a glimpse of {weapon}.",
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
    {"name":sydney.display_name(),
     "val" : sydney.display(),
     "room": sydney.display_mroom(),
     "intro": "\nHey! There seems to be a lot of commotion this morning, right? [awkward chuckle]\n-----",
     "initial_1" : "\nSorry? Is there something that happened?\n-----",
     "initial_2" : "\nNothing much! Just the rain... falling down... down... and down...\nI also did find {weapon} when looking around {room}, right after {person} walked out!\nNot sure why you'd need to know that, though.\n----- ",
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
    {"name":house.display_name(),
     "val" : house.display(),
     "room": house.display_mroom(),
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
    {"name":kevin.display_name(),
     "val" : kevin.display(),
     "room": kevin.display_mroom(),
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
]


weapon = ["The bag", "Pallete Knife", "Trombone", "Cafeteria Spoon", "Bag of Bricks", "Scurvy Potion", "Sword", "Wizard's Curse"]

count=0
murderer_choose = random.choice(chars)
while count < 10:
    count+=1
    chars.append(murderer_choose)
count=0
murderer = murderer_choose["name"]
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