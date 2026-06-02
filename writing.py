Journal = []
def ReadJournal():
    print("In your notebook, you have written..")
    for index, line in enumerate(Journal):
        print("Entry", index, ":", line)
        print("~")
    if len(Journal) == 0:
        print("You haven't written anything down yet!")


def WRITETHATDOWN():
    WritingNow = True  
    while WritingNow == True:
        newline = (str(input("What would you like to write down?:")))
        Journal.append(newline)
        wannawrite = (str(input("Would you like to write more? Yes, or No?:"))).capitalize()
        if "No" == wannawrite:
            WritingNow = False
            print("Your Marble Notebook will dutifully keep all of your observations. It seems it is the only one you can depend on in these times.")
        elif "Yes" == wannawrite: 
            WritingNow = True
        else:
            print("Your pen clatters to the floor as you drop it. You have stopped writing.")
            WritingNow = False

yaona = ["Yes", "No"]
def inspectjuli():
    print("Julius is in this room. Do you wish to look closer?")
    for index, option in enumerate(yaona):
        print(index, ":", option)
    choice = int(input("Enter the corresponding integer:"))
    if choice == 0:
        print("You step over to where she lies.")
    else:
        print("Whether it be from confusion, fear, disgust, or indifference, you avert your eyes.")

inspectjuli()