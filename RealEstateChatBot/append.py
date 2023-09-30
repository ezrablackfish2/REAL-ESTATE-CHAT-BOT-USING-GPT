import json

def systemappender(messages, my_id):
    system_create = {
            f"{my_id}": [
                {
            "role": "system",
            "content": "You are a Real Estate AI assistant only and only anything other than our real estate is asked just say sorry but i am only a real estate AI assistant you only assist user with our real estate intense description and the service it provides and the prices of the specific things like the houses, furnitures in it, the rooms, the location say i am sorry whenever unrelated to our real estate comes up like if someone says what is psychology you say sorry but i am only a Real Estate AI assistant",
            }
            ]
            }
    filename = "context.json"
    str_id = str(my_id)
    with open(filename, "r") as f:
        convo = json.load(f)

    
    str_id = str(my_id)
    if (str_id in convo):
        messages = convo[str_id]
        messages.append(system_create[str_id][0])
        convo[str_id] = messages


        if (True):
            with open(filename, "w") as file:
                convo = json.dump(convo, file)
                file.close()

    else:
        messages.append(system_create[str_id][0])
        convo[str_id] = messages
        with open(filename, "w") as file:
            json.dump(convo, file)
            file.close()
    f.close()
    return(messages)

def userappender(prompt, messages, my_id):
    current_message = {
            "role": "user",
            "content": prompt,
            }

    filename = "context.json"
    with open(filename, "r") as file:
        convo = json.load(file)
    
    str_id = str(my_id)
    messages = convo[str_id]
    messages.append(current_message)
    convo[str_id] = messages
    last = convo[str_id]

    with open(filename, "w") as file:
        convo = json.dump(convo, file)
        file.close()
    return(last)

def assistantappender(response, messages, my_id):
    current_response = {
            "role": "assistant",
            "content": response,
            }
    filename = "context.json"
    with open(filename, "r") as file:
        convo = json.load(file)

    str_id = str(my_id)
    messages = convo[str_id]
    messages.append(current_response)
    convo[str_id] = messages
    last = convo[str_id]

    with open(filename, "w") as file:
        convo = json.dump(convo, file)
        file.close()
    return(last)

