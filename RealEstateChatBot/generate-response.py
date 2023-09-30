import openai
import json
import time
from functionDescription import function_description
from caller import function_call 

KEY = "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"
openai.api_key = KEY


def generate_response(messages, my_id):
    print(messages)
    try:
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613",
                messages=messages,
                functions=function_description,
                function_call="auto",
                temperature = 0.9
                )
    except:
        time.sleep(20)
        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0613",
                    messages=messages,
                    functions=function_description,
                    function_call="auto",
                    temperature=0.9
                    )
    while response["choices"][0]["finish_reason"] == "function_call":
            function_response = function_call(response, my_id)
            result = json.dumps(function_response)
            messages.append({
                "role": "function",
                "name": response["choices"][0]["message"]["function_call"]["name"],
                "content": response["choices"][0]["message"]["function_call"]['arguments']
                })

            messages.append({
                "role": "function",
                "name": response["choices"][0]["message"]["function_call"]["name"],
                "content": function_response
                })


    while True:
        try:
                    response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo-0613",
                            messages=messages,
                            functions = function_description,
                            function_call="auto",
                            temperature = 0.9
                            )
                    break
        except openai.error.RateLimitError:
                    print("you have reached your maximum limit")
                    time.sleep(20)
    return response
