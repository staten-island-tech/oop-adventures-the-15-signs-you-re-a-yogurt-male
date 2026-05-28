# welcome 
import random
# first murderer EVER generated: mr. whalen 
Murderedrooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium" ]
character_list = ["fulgrim", "house","whalen", "jon","wizard","kevin","cecil","sydney"]

def initialize():
    
    Body_Room = random.choice(Murderedrooms_list)
    Murderer = random.choice(character_list)

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
    f"Those thoughts were then proven wrong, when one of your classmates, Julius, was found dead in {Body_Room}.",
 ]
    for line in intro_writing: 
         print(line)
    if input("Press anything and then the Enter Key to continue: "):
        print("Intro Complete!")
        
class detective:
    def __init__(self, pname, interactedtoday,CanSleep,daysleft,TotalEnergy,CanAct):
         self.pname = pname
         self.interactedtoday = interactedtoday
         self.CanSleep = CanSleep
         self.daysleft = daysleft
         self.TotalEnergy = TotalEnergy 
         self.CanAct = CanAct

    def checkinteraction(self):
        self.CanSleep = False
        if self.interactedtoday > 0:
            self.CanSleep = True
        else:
            self.CanSleep = False
            
    def checkenergy(self):
        if self.TotalEnergy <= 0:
            self.CanAct = False
        else:
            self.CanAct = True

    def raiseinteractioncount(self):
        self.TotalEnergy -= 1
        self.interactedtoday += 1

    def bedtime(self):
         self.daysleft -= 1
         print(f"You have {self.daysleft} days left to find Julius's killer.")
         self.interactedtoday = 0
         self.TotalEnergy = 5
         self.CanSleep = False


play = detective(str(input("Welcome! Before the game begins, please state your name: ")),0,False,3,5,True)
