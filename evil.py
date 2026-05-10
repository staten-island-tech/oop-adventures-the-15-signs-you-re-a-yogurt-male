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
        info = (f"Murderer: {self.full_name}\nRoom: {self.room}\nWeapon: {self.weapon}")
        return info
    
def weaponn():
    w = random.choice(weapon)
    weapon.remove(w)
    return (w)

cecil= char("Cecil Gershwin Palmer", "Cecil", random.choice(room), weaponn())
fulgrim= char("Fulgrim", "Fulgrim", random.choice(room), weaponn())
jon= char("Jonathan Sims", "Jon", random.choice(room), weaponn())
whalen = char("Mr. Whalen", "Mr. Whalen", random.choice(room), weaponn())
wizard = char("The Wizards is an Animal", "Wizard", random.choice(room), weaponn())
sydney = char("Sydney Sargent", "Sydney", random.choice(room), weaponn())
house = char("Dr. Gregory House", "House", random.choice(room), weaponn())
kevin = char("The Great and Mighty Kevin", "Kevin", random.choice(room), weaponn())

characters = [
    {"name": "cecil",
     "val": cecil.display()},
    {"name": "fulgrim", 
     "val" : fulgrim.display()},
    {"name": "jon",
     "val" : jon.display()},
    {"name":"whalen",
     "val" : whalen.display()},
    {"name":"wizard",
     "val" : wizard.display()},
    {"name":"sydney",
     "val" : sydney.display()},
    {"name":"house",
     "val" : house.display()},
    {"name":"kevin",
     "val" : kevin.display()},
]

murder = random.choice(characters)
print(murder["val"])