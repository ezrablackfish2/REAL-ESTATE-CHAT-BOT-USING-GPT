import json

def function_call(response,id_):

    
    function_call = response["choices"][0]["message"]["function_call"]
    function_name = function_call["name"]
    function_args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])
    

    with open("data.json", "r") as file:
            data = json.load(file)



    if function_name == "getDescription":
        arg = function_args["kind"]
        if arg == "title":
            return data["title"]
        if arg == "description":
            return data["description"]
        if arg == "history":
            return data["history"]
        if arg == "location['overall']":
            return data["location"]["overall"]
        if arg == "location['addis ababa']":
            return data["location"]["addis ababa"]
        if arg == "location['nazret']":
            return data["location"]["nazret"]
        if arg == "location['bahirdar']":
            return data["location"]["bahirdar"]
        if arg == "location['arbamich']":
            return data["location"]["arbaminch"]
        if arg == "location['mekelle']":
            return data["location"]["mekelle"]
        if arg == "lcoation['jimma']":
            return data["lcoation"]["jimma"]
        if arg == "safety & hazard":
            return data["safety & hazard"]
        if arg == "contact":
            return data["contact"]
        if arg == "contact['email']":
            return data["contact"]["email"]
        if arg == "contact['twitter']":
            return data["contact"]["twitter"]
        if arg == "contact['telegram']":
            return data["contact"]["telegram"]
        if arg == "price['rent']":
            return str(data["price"]["rent"])
        if arg == "price['purchase']":
            return str(data["[price"]["purchase"])
        if arg == "price":
            return str(data["price"])
        if arg == "amneties":
            return str(data["amneties"])
        if arg == "amneties['livingroom']":
            return data["amneties"]["livingroom"]
        if arg == "amneties['bathroom']":
            return data["amneties"]["bathroom"]
        if arg == "amneties['kitchen']":
            return data["amneties"]["kitchen"]
        if arg == "amneties['balcony']":
            return data["amneties"]["balcony"]
        if arg == "amneities['mainbedroom']":
            return data["amneties"]["mainbedroom"]
        if arg == "amneities['guestbedroom']":
            return data["amneties"]["guestbedroom"]
        if arg == "amneties['garage']":
            return data["amneties"]["garage"]
        if arg == "amneties['storingattic']":
            return data["amneties"]["storingattic"]
        if arg == "amneities['dinningroom']":
            return data["amneties"]["dinningroom"]
        if arg == "amneties['outdoor']":
            return data["amneties"]["outdoor"]
        if arg == "rooms":
            return str(data["rooms"])
        if arg == "rooms['livingroom']":
            return data["rooms"]["livingroom"]
        if arg == "rooms['mainbedroom']":
            return data["rooms"]["mainbedroom"]
        if arg == "rooms['kitchen']":
            return data["rooms"]["kitchen"]
        if arg == "rooms['balcony']":
            return data["rooms"]["balcony"]
        if arg == "rooms['guestbedroom']":
            return data["rooms"]["guestbedroom"]
        if arg == "rooms['dinningroom']":
            return data["rooms"]["dinningroom"]
        if arg == "rooms['garage']":
            return data["rooms"]["garage"]
        if arg == "rooms['storingattic']":
            return data["rooms"]["storingattic"]
        if arg == "rooms['bathroom']":
            return data["rooms"]["bathroom"]
        if arg == "services":
            return data["services"]
        if arg == "availability":
            return data["availability"]
        if arg == "images":
            return data["images"]
