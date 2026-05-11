import random

rooms = ["Cafeteria", "Compsci Lab", "Auditorium", "Secret pool on the roof", "Engineering Henriques", "Gym", "Goyco Russian"]
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
    def display_name(self):
        return self.full_name
    def display_mroom(self):
        return self.room
    def display_mweapon(self):
        return self.weapon
    
def weaponn():
    w = random.choice(weapon)
    weapon.remove(w)
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
     "room": cecil.display_mroom()},
    {"name": fulgrim.display_name(), 
     "val" : fulgrim.display(),
     "room": fulgrim.display_mroom()},
    {"name": jon.display_name(),
     "val" : jon.display(),
     "room": jon.display_mroom()},
    {"name":whalen.display_name(),
     "val" : whalen.display(),
     "room": whalen.display_mroom()},
    {"name":wizard.display_name(),
     "val" : wizard.display(),
     "room": wizard.display_mroom()},
    {"name":sydney.display_name(),
     "val" : sydney.display(),
     "room": sydney.display_mroom()},
    {"name":house.display_name(),
     "val" : house.display(),
     "room": house.display_mroom()},
    {"name":kevin.display_name(),
     "val" : kevin.display(),
     "room": kevin.display_mroom()},
]

murder = random.choice(chars)
#print(murder["val"])