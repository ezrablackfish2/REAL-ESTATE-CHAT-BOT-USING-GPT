import json

def reset(my_id):
    reseted = [
            {
                "role": "system",
                "content": "You are a hotel AI assistant only and only anything other than our hotel is asked just say sorry but i am only a hotel AI assistant you only assist user with our hotel say i am sorry whenever unrelated to our hotel comes up like if someone says what is psychology you say sorry but i am only a hotel AI assistant"
            }
            ]
    filename= "context.json"
    with open(filename, "r") as file:
        convo = json.load(file)
    str_id = str(my_id)
    convo[str_id] = reseted

    with open(filename, "w") as file:
        json.dump(convo, file)
    
    file.close()
    print("sir we have succesfully resetted your conversation")
