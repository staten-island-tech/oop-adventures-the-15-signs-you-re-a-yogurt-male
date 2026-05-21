def CHECKFORINTEGER(ourinput):
    try: 
            number = int(ourinput)
    except ValueError:
        print("Invalid input! Reread the above instructions.")
class detective:
    def __init__(player_name,self, interactedtoday,CanSleep,daysleft,TotalEnergy,CanAct):
         self.player_name = player_name
         self.interactedtoday = interactedtoday
         self.CanSleep = CanSleep
         self.daysleft = daysleft
         self.TotalEnergy = TotalEnergy 
         self.CanAct = CanAct

    def checkinteraction(self):
        self.CanSleep = False
        if self.interactedtoday > 0:
            self.CanSleep = True
            
    def checkenergy(self):
        if self.TotalEnergy <= 0:
            CanAct = False
        else:
            CanAct = True 


player = detective((input("Welcome! Before the game begins, please state your name: ")),0,False,3,5,True)
