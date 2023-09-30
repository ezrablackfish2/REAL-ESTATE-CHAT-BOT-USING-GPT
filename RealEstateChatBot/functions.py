import json
filename = "data.json"
with open(filename, "r") as file:
    data = json.load(file)
file.close()

def getTitle():
    return(data["title"])

def getHistory():
    return(data["history"])
def getDescription():
    return(data["description"])
def getLocation():
    return(data["location"])
def getRules():
    return(data["rules"])
def getServices():
    return(data["services"])
def getBed():
    return(data["services"])
def getFood(kind):
    return(data["food"][kind])
def getEntertainment():
    return(data["entertainment"])
def getPrice(service):
    return(data["price"][service])
def getAmneties(room):
    return(data["amneties"][room])
def getContact(kind):
    return(data["contact"][kind])
def getAvailability():
    return(data["avaiability"])
def getImages():
    return(data["images"])
def getRooms(room):
    return(data["rooms"][room])
def safety():
    return(data["safety & Hazard"])
def getInfoCancel():
    return(data["cancellation on booking"])
def getPrivacy():
    return(data["privacy policy"])
