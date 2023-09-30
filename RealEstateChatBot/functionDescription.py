function_descriptions = [
        {
            "name": "getDescription",
            "description": "general information of the real estate including the real estate's title, description, history, location and information about the rooms , amneties, images about the real estate and about the price of the houses and finally safety precautions of the real estate, contact you can get to the real estate and its owners and always remember when asked about contact room and amnety always require specifically ask them that there is no general",
            "parameters" : {
                "type": "object",
                "properties": {
                    "kind": {
                        "type": "string",
                        "enum": ["title", "description", "history", "services","location['overall']", "location['addis ababa']", "location['nazret']","location['bahirdar']", "location['arbamich']", "location['mekelle']", "lcoation['jimma']", "safety & Hazard", "contact['email']", "contact['website']", "contact['phone number']", "contact['twitter']", "contact['telegram']", "price['rent']", "price['purchase']", "amneties['livingroom']", "amneties['bathroom']", "amneties['kitchen']", "amneties['balcony']", "amneities['mainbedroom']", "amneities['guestbedroom']", "amneties['garage']","amneties['storingattic']", "amneities['dinningroom']", "amneties['outdoor']", "rooms['mainbedroom']" , "rooms['guestbedroom']","rooms['livingroom']", "rooms['balcony']", "rooms['kitchen']", "rooms['dinningroom']", "rooms['garage']", "rooms['storingattic']", "rooms['bathroom']", "price['rent']", "price['purchase']", "availablity", "images"],
                        "description": "the type of information about the real estate like title, description, history, location, safety things that the user should know and price contact room amnety"
                        },
                    },
                "required": ["kind"],
                }
            }
] 
