import evil
import writing # imports writing system
from playerclass import play
from evil import murder_room
from murderer import bodyfacts
# from main import initialize
# from murderer import inspectjuli
actionswpeople = ["See room", "Leave Room", "Write Clues Down", "Check Notebook","Interact","Leave Room and Return to Supply Closet [SLEEP]"]
# actionswnpp = ["See room", "Leave Room", "Write Clues Down", "Check Notebook"]
def people(room):
    p_list = []
    for char in evil.chars:
        if char["room"] == room:
            p_list.append(char["codeterm"])
    # print(p_list)
    return p_list
 


class room:
    def __init__(self, name, desc, people):
        self.name = name
        self.desc = desc
        self.people = people
    def display_room(self):
        p_list = []
        for person in self.people:
            p_list.append(person.display_name())
        info = (f"You are now in {self.name}.\n{self.desc}\nPeople:{p_list}")
        return info
    def show_room(self):
        #insert code for image display
        print("room shown")

    def printpeople(self):
        if len(self.people) <= 0: 
            (self.people).append("Nobody")
            print("There is nobody here to speak to.")
        else:
            p_list = []
            for person in self.people:
                p_list.append(person.display_name())
            info = (f"You are now in {self.name}.\n{self.desc}\nPeople:{p_list}")
            for indexnumb, person in enumerate(self.people):
                print(indexnumb, ":", person.display_name())
            speak = int(input("Who would you like to speak to?"))
            evil.interact(speak, p_list)
   
    def countpeople(self):
        peoplecount = len(self.people)
        if peoplecount <= 0:
            anyppl = False
caf = room("Cafeteria",
           "Most of the usually blinding lights are off, with a few flickering lazily, providing just enough light for you to see. " \
           "Through the basement windows you can see water leaking through, though not enough to flood the cafeteria yet. ",
           people("Cafeteria"))
compsci = room("Compsci Lab",
            "The room is filled with an eerie light, as thick clouds block any sun from illuminating the space. " \
            "You peer around the rows of computers, looking for any people or clues. ",
            people("Compsci Lab"))
aud = room("Auditorium",
            "The auditorium feels much bigger than it should, rows upon row of seats leading to an eventual stage. " \
            "A crack of thunder can be heard outside, with rain pounding down on each of the many windows. ",
            people("Auditorium"))
pool = room("Secret pool on the roof",
            "You thought this place was only a rumor spread by seniors, yet here it stands. " \
            "Clearly not having been maintained for a long time, rainwater fills the pit, not quite overflowing yet. ",
            people("Secret pool on the roof"))
engineering = room("Engineering Henriques",
            "Strangely, this room does have a single light turned on, unlike the other rooms. " \
            "You are thankful, for you would not have been able to see inside this basement room otherwise at all. " \
            "Forgotten projects litter the floor and tabletops, alongisde many tools that could certainly be used to injure. ",
            people("Engineering Henriques"))
gym = room("Gym",
            "The gym is a vast space, lined with cold and empty bleachers on either side. " \
            "The only light comes from the rain-washed windows, waterfalls streaming down them and distorting whatever hasn't been blocked out by thick, grey clouds. ",
            people("Gym"))
goyco = room("Goyco Russian",
            "For some indescernible reason, the air conditioner in this room runs as though there is no storm at all. " \
            "As you listen to it rattle on, you see the desks disturbed and several overturned chairs. " \
            "The last person to have been in this room must have really made an effort to show their dislike of it. ",
            people("Goyco Russian"))
supplycloset = room("Supply Closet", "HONK SHOOOO MIMIMI.", [])

rooms = [
    {"name": "Cafeteria", "codeterm": caf, 
     "disp": caf.display_room()}, 
    {"name": "Compsci Lab", "codeterm": compsci,
     "disp": compsci.display_room()}, 
    {"name": "Auditorium", "codeterm": aud,
     "disp": aud.display_room()},
    {"name": "Secret pool on the roof", "codeterm": pool, 
     "disp": pool.display_room()},
    {"name": "Engineering Henriques", "codeterm": engineering, 
     "disp": engineering.display_room()},
    {"name": "Gym", "codeterm": gym, 
     "disp": gym.display_room()},
    {"name": "Goyco Russian", "codeterm": goyco, 
     "disp": goyco.display_room()}, 
    # {"name": "The Supply Closet", "codeterm": supplycloset, "disp": "" }
    
    ]


global roomneeded
global roomwithin
roomwithin = "nowhere"
roomneeded = "placeholder, not yet updated"
def go_to_sleep():
            play.checkinteraction()
            if play.CanSleep == False: 
                print("Are you genuinely trying to go back to sleep without doing anything? Get back out there!")
                enterroom()
            else:
                    print("After deciding you're done with your investigation, you retire for the day.")
                    print("~")
                    print("You awake the next morning, still unfortunately trapped.")
                    play.bedtime()
    #                 if days > 0:
    #                     enterroom()
    #                 else: 
    #                     print()
    #                     print("Your time has ran out. You need to determine who the murder is, and with the info your investigation collected, "
    # "convince your peers to barricade them away before they come after you.")

def enterroom():
    global murder_room
    location = "none"
    sleeping = False
    while location == "none":
        play.checkenergy()
        for index, item in enumerate(rooms):
            print(f"{index}: {item["name"]}")
        c_location = (input("What room would you like to enter? Please enter a number:  "))
        c_location = int(c_location)
        if c_location > 6 or c_location < 0:
             print("Not a valid room.")
             c_location = (input("What room would you like to enter? Please enter a number:  "))
             c_location = int(c_location)
        location = rooms[c_location]
        print(location["disp"])
        global roomneeded 
        global roomwithin
        roomneeded = location["codeterm"]
        roomwithin = location["name"]
        print(roomwithin, murder_room)
        
def inspectjuli():
     global murder_room
     global roomwithin
     yaona = ["Yes", "No"]
     if murder_room == roomwithin:
        print("Julius is in this room. Do you wish to look closer?")
        for index, option in enumerate(yaona):
            print(index, ":", option)
        choice = int(input("Enter the corresponding integer:"))
        if choice == 0:
         print("You step over to where she lies.")
         bodyfacts()
        else:
         print("Whether it be from confusion, fear, disgust, or indifference, you avert your eyes.")

def makeanaction():
        global murder_room
        global roomneeded
        global roomwithin 
        a = False
        while a == False:
            for index, action in enumerate(actionswpeople):
                print(f"{index}: {action}")
            act = int(input("What would you like to do?:"))
            if act == 0:
                play.checkenergy()
                if play.CanAct == False:
                    print("Your thoughts are slowed by fatigue and your eyes are unable to focus on the details of the room around you. Get some rest!")
                else:
                    play.raiseinteractioncount()
                    print("displaying tkinter window")
                    inspectjuli()
            elif act == 1:
                print("You have left the room.")
                enterroom()
            elif act == 2:
                print("You take out your trusty Marble Notebook and Pen.")
                writing.WRITETHATDOWN()
            elif act == 3:
                writing.ReadJournal()
            elif act == 4:
                play.checkenergy()
                if play.CanAct == False:
                    print("Your thoughts are slowed by fatigue and you fail, horribly, to properly converse with anyone. Get some rest!")
                else:
                 play.raiseinteractioncount()
                 roomneeded.printpeople()
            elif act == 5: 
                go_to_sleep()
                return "BEDDED_TIME"

         

# MEAT ABOVE ^^^ Below.. Succint version of what is being done. 

#calling! !
