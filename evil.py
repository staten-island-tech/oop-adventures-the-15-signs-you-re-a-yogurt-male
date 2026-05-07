import random

murderer = [True, False]
room = ["Cafeteria", "Compsci Lab", "Auditorium", "Secret pool on the roof", "Engineering Henriques", "Gym", "Goyco Russian"]
weapon = ["The bag", "Pallete Knife", "Trombone", "Cafeteria Spoon", "Bag of Bricks", "Scurvy Potion", "Sword", "Wizard's Curse"]
class char:
    def __init__(self, full_name, first_name, gulit, room, weapon):
        self.full_name = full_name
        self.first_name = first_name
        self.guilt= gulit
        self.room = room
        self.weapon = weapon
    def display(self):
        print(self.name, self.guilt, self.room, self.weapon)

characters = [
    {"cecil": char("Cecil Gershwin Palmer", "Cecil", random.guilty(), random.room(), random.weapon)},
    {"fulgrim" : char("Fulgrim", "Fulgrim", random.guilty(), random.room(), random.weapon)},
    {"jon" : char("Jonathan Sims", "Jon", random.guilty(), random.room(), random.weapon)},
    {"whalen" :char("Mr. Whalen", "Mr. Whalen", random.guilty(), random.room(), random.weapon)},
    {"wizard" : char("The Wizards is an Animal", "Wizard", random.guilty(), random.room(), random.weapon)},
    {"sydney" : char("Sydney Sargent", "Sydney", random.guilty(), random.room(), random.weapon)},
    {"house" : char("Doctor House", "House", random.guilty(), random.room(), random.weapon)},
    {"kevin" : char("The Great and Mighty Kevin", "Kevin", random.guilty(), random.room(), random.weapon)},
]

