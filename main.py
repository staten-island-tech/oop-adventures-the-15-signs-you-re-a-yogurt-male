# hallway goal: select list of names.. ect
def movethru():
    rooms_list = ["Cafeteria","Compsci Lab", "Goyco Room", "Gymnasium", "Library", "Henriques Engineering", "Secret pool on the roof","Auditorium"]
    for index, x in enumerate(rooms_list):
            print(index, ":", x)
movethru()