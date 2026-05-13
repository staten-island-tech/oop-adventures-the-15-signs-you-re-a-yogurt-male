def CHECKFORINTEGER(ourinput):
    while True:
        try: 
            num = int(ourinput)
            break
    except ValueError:
        print("Invalid input!")

print(num)