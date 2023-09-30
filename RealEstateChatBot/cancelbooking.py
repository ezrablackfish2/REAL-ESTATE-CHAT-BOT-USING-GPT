import requests 
import json

def cancelbooking(my_id, room_id):
    id =1
    result = requests.get(f"http://127.0.0.1:8000/api/{id}")
    print(result)
    room = result.json()
    print(room)
    room["subtitle"] = "unbooked"
    room["isbn"] = f"{my_id}"
    print(room["subtitle"])
    result = requests.put(f"http://127.0.0.1:8000/api/{id}", json=room)
    print(result)
cancelbooking(72, 102)
