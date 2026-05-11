Journal = []
def ReadJournal():
    print("In your notebook, you have written..")
    for line in Journal:
        print(line)
        print("~~~")
    if len(Journal) == 0:
        print("You haven't written anything down yet!")


def WRITETHATDOWN():
    WritingNow = True  
    while WritingNow == True:
        newline = (str(input("What would you like to write down?:")))
        Journal.append(newline)
        if "No" == (str(input("Would you like to write more? Yes, or No?:"))).capitalize():
            WritingNow = False
            print("Your Marble Notebook will dutifully keep all of your observations. It seems it is the only one you can depend on in these times.")
        else: 
            WritingNow = True
