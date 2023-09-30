from functions import getTitle
import json

def function_call(response, my_id):
    function_call = response["choices"][0]["message"]["function_call"]
    function_name = function_call["name"]
    function_args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])

    if function_name == "getFood":
        arg = function_args["kind"]

        if arg == "fasting":
            food = getFood("fasting")
        if arg == "non-fasting":
            food = getFood("non-fasting")
        if arg == "drinks":
            food = getFood("drinks")
        else:
            food = "please choose between the type of food fasting non-fasting and drinks"
        return (food)
    if function_name == "getPrice":
        arg = function_args["service"]

        if arg == "food":
            price = getPrice("food")
        if arg == "bed":
            price = getPrice("bed per day")
        if arg == "hot shower":
            price = getPrice("hot shower")
        if arg == "gym":
            price = getPrice("gym per day")
        else:
            price = "please choose the price between food bed hot shower or gym"
        return (price)

    if function_name == "getAmneties":
        arg = function_args["room"]

        if arg == "livingroom":
            amnety = getAmneties("livingroom")
        if arg == "bedroom":
            amnety = getAmneties("bedroom")
        if arg == "bathroom":
            amnety = getAmneties("bathroom")
        if arg == "kitchen":
            amnety = getAmneties("kitchen")
        if arg == "balcony":
            amnety = getAmneties("balcony")
        else:
            amnety = "please choose between livingroom, bedroom, bathroom, kitchen or balcony"
        return amnety


    if function_name == "getTitle":
        title = getTitle()
        return (f"our hotel is known as {title}")
    if function_name == "getHistory":
        history = getHistory()
        return (history)
    if function_name == "getDescription":
        description = getDescription()
        return (description)
    if function_name == "getLocation":
        location = getLocation()
        return (location)
    if function_name == "getRules":
        rules = getRules()
        return (rules)
    if function_name == "getServices":
        services = getServices()
    if function_name == "getBed":
        bed = getBed()
        return (bed)
    if function_name == "getEntertainment":
        entertainment = getEntertainment()
        return (entertainment)
    if function_name == "getAvailability":
        availability = getAvailability()
        return (availability)
    if function_name == "safety":
        safe = safety()
        return (safe)
    if function_name == "getInfoCancel":
        info = getInfoCancel()
        return (info)
    if function_name == "getPrivacy":
        privacy = getPrivacy()
        return (privacy)

