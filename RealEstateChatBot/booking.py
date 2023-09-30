import requests
from room import findRoom
import json

def booking(my_id):
    id = 1
    result = requests.get(f"http://127.0.0.1:8000/api/{id}")
    updated = {
            "title": "the alchemy",
            "subtitle": "alchemy",
            "author": "the arabian peninsula",
            "isbn": "929201293"
            }
    result = requests.put(f"http://127.0.0.1:8000/api/{id}", json=updated)
    id = 9
    result = requests.delete(f"http://127.0.0.1:8000/api/{id}")
    result = requests.get(f"http://127.0.0.1:8000/api/")
    room = result.json()
    print(result)
    freeRoom = []
    i = 0
    while i < len(room):
        for j, k in room[i].items():
            if k == "booked":
                freeRoom.append(room[i])
        i = i + 1
    return (freeRoom)
booking(72);
