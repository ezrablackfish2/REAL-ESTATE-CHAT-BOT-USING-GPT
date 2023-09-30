import json

def findRoom():
    free = []
    filename = "rooms.json"
    try:
        with open(filename, "r") as file:
            json.load(file)
            file.close()
    except:
        create = {
                "room 101": "unbooked",
                "room 102": "booked",
                "room 103": "unbooked",
                "room 104": "booked",
                "room 105": "unbooked"
                }
        with open(filename, "w") as file:
            json.dump(create, file)
            file.close()

    with open(filename, "r") as file:
        convo = json.load(file)

    for i, j in convo.items():
        if (j == "unbooked"):
            free.append(i)
    for k in free:
        print(k)
    return(free)

