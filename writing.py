Journal = []
def ReadJournal():
    for line in Journal:
        print(line)
        print("~~~")


def WRITETHATDOWN():
    WritingNow = True  
    while WritingNow == True:
        newline = (str(input("What would you like to write down?:")))
        Journal.append(newline)
        if "No" == (str(input("Would you like to write more? Yes, or No?:"))).capitalize():
            WritingNow = False
        else: 
            WritingNow = True
