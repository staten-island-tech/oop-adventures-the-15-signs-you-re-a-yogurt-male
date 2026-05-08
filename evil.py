import random

room = ["Cafeteria", "Compsci Lab", "Auditorium", "Secret pool on the roof", "Engineering Henriques", "Gym", "Goyco Russian"]
weapon = ["The bag", "Pallete Knife", "Trombone", "Cafeteria Spoon", "Bag of Bricks", "Scurvy Potion", "Sword", "Wizard's Curse"]
class char:
    def __init__(self, full_name, first_name, room, weapon):
        self.full_name = full_name
        self.first_name = first_name
        self.room = room
        self.weapon = weapon
    def display(self):
        print(self.full_name, self.room, self.weapon)

""" characters = [
    {"cecil": char("Cecil Gershwin Palmer", "Cecil", random.choice(room), random.choice(weapon))},
    {"fulgrim" : char("Fulgrim", "Fulgrim", random.choice(room), random.choice(weapon))},
    {"jon" : char("Jonathan Sims", "Jon", random.choice(room), random.choice(weapon))},
    {"whalen" :char("Mr. Whalen", "Mr. Whalen", random.choice(room), random.choice(weapon))},
    {"wizard" : char("The Wizards is an Animal", "Wizard", random.choice(room), random.choice(weapon))},
    {"sydney" : char("Sydney Sargent", "Sydney", random.choice(room), random.choice(weapon))},
    {"house" : char("Doctor House", "House", random.choice(room), random.choice(weapon))},
    {"kevin" : char("The Great and Mighty Kevin", "Kevin", random.choice(room), random.choice(weapon))},
] """

characters = [
    {"name": "cecil",
     "val": char("Cecil Gershwin Palmer", "Cecil", random.choice(room), random.choice(weapon))},
    {"name": "fulgrim", 
     "val" : char("Fulgrim", "Fulgrim", random.choice(room), random.choice(weapon))},
    {"name": "jon",
     "val" : char("Jonathan Sims", "Jon", random.choice(room), random.choice(weapon))},
    {"whalen" :char("Mr. Whalen", "Mr. Whalen", random.choice(room), random.choice(weapon))},
    {"wizard" : char("The Wizards is an Animal", "Wizard", random.choice(room), random.choice(weapon))},
    {"sydney" : char("Sydney Sargent", "Sydney", random.choice(room), random.choice(weapon))},
    {"house" : char("Doctor House", "House", random.choice(room), random.choice(weapon))},
    {"kevin" : char("The Great and Mighty Kevin", "Kevin", random.choice(room), random.choice(weapon))},
]

""" cecil= char("Cecil Gershwin Palmer", "Cecil", random.choice(room), random.choice(weapon))
fulgrim= char("Fulgrim", "Fulgrim", random.choice(room), random.choice(weapon))
jon= char("Jonathan Sims", "Jon", random.choice(room), random.choice(weapon))
whalen = char("Mr. Whalen", "Mr. Whalen", random.choice(room), random.choice(weapon))
wizard = char("The Wizards is an Animal", "Wizard", random.choice(room), random.choice(weapon))
sydney = char("Sydney Sargent", "Sydney", random.choice(room), random.choice(weapon))
house = char("Doctor House", "House", random.choice(room), random.choice(weapon))
kevin = char("The Great and Mighty Kevin", "Kevin", random.choice(room), random.choice(weapon))

characters = {
    "cecil": cecil.__init__,
    "fulgrim": fulgrim.__init__, 
    "jon": jon.__init__,
    "whalen": whalen.__init__, 
    "wizard": wizard.__init__, 
    "sydney": sydney.__init__,
    "house": house.__init__, 
    "kevin": kevin.__init__
} """

""" characters = [cecil, fulgrim, jon, whalen, wizard, sydney, house, kevin]
 """
murderer = random.choice(characters)
murderer.display()
#print(murderer)