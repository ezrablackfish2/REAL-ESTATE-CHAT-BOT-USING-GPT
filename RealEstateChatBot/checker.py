import json

def fileChecker(my_id):
    filename = "context.json"
    str_id = str(my_id)
    try:
        with open(filename, "r") as file:
            json.load(file)
            file.close()
    except:
        create = {
                f"{str_id}": []
                }
        with open(filename, "w") as file:
            json.dump(create, file)
            file.close()
