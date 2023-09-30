import json

def function_call(response,id_):

    
    function_call = response["choices"][0]["message"]["function_call"]
    function_name = function_call["name"]
    function_args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])
    

    with open("properties.json", "r", encoding="utf-8") as f:
            properties = json.load(f)

    with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)


    global imageType
    global imgs
    global random_imgs

    if function_name == 'get_information':
        if function_args['about'] == 'Sweat Fitness Studio':
            imageType = 'image'
            imgs = properties['images']["Sweat Fitness Studio"]
            random_imgs = imgs

            return data["title"]
        arg = function_args['about']
        return properties[arg]

    if function_name == 'offerings':
        if function_args['about'] == 'Sweat Fitness Studio offerings':

            imageType = 'image'
            imgs = properties['images']["offerings"]["description"]
            random_imgs = image_randomizer(imgs)

            return properties['offerings']["description"]

        arg = function_args['about']
        imageType = 'image'
        imgs = properties['images']["offerings"][arg]
        random_imgs = image_randomizer(imgs)

        return properties['offerings'][arg]


    if function_name == 'classes':
        if function_args['about'] == 'Sweat Fitness Studio Classes':

            imageType = 'image'
            imgs = properties['images']["classes"]["description"]
            random_imgs = image_randomizer(imgs)

            return properties['classes']["description"]

        arg = function_args['about']

        imageType = 'image'
        imgs = properties['images']["classes"][arg]
        random_imgs = image_randomizer(imgs)

        return properties['classes'][arg]   

    if function_name == 'pricing':
        return properties['pricing']
