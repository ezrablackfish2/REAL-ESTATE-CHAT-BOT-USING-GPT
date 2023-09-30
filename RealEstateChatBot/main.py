from response import response
from user import my_user
from append import userappender, systemappender, assistantappender
import json
from checker import fileChecker
from reset import reset
from functionDescription import function_descriptions
from AIresponse import generate_response

def hotelbot(my_user):
    messages = []
    my_id = my_user.chat.id 
    fileChecker(my_id)
    systemappender(messages, my_id)
    while (my_user.text != "stop"):
        prompt = input("your conversation: ")
        my_user.text = prompt
        if (prompt == "reset"):
            reset(my_id)
        last_user = userappender(prompt, messages, my_id)
        final = generate_response(last_user, my_id)
        final_response = final["choices"][0]["message"]["content"]
        print(final_response)
        print(final)
        last_AI = assistantappender(final_response, messages, my_id)
hotelbot(my_user)



