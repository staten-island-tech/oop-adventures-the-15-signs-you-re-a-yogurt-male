def CHECKFORINTEGER(ourinput):
    try: 
            number = int(ourinput)
    except ValueError:
        print("Invalid input! Reread the above instructions.")
