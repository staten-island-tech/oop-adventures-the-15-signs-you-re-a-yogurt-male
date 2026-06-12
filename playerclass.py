class detective:
    def __init__(self, pname, interactedtoday,CanSleep,TotalEnergy,CanAct):
         self.pname = pname
         self.interactedtoday = interactedtoday
         self.CanSleep = CanSleep
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
         self.interactedtoday = 0
         self.TotalEnergy = 5
         self.CanSleep = False

play = detective(str(input("Before we begin, what is your name?:")),0, False, 3, True)