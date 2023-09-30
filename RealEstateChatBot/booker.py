import requests
from booking import booking
import json

def booker(my_id, room_id):
    id = 1
    result = requests.get(f"http://127.0.0.1:8000/api/{id}")
    print(result)
    room = result.json()
    room["subtitle"] = "booked"
    room["isbn"] = f"{my_id}"
    result = requests.put(f"http://127.0.0.1:8000/api/{id}", json=room)
    print(result)

booker(72, 102)
