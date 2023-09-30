import openai
import json
import time
from functionDescription import function_descriptions
from caller import function_call
import openai
import json
import time
import openai
import json
import requests
import random
import datetime

KEY = "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"
openai.api_key = KEY


def generate_response(messages,id_):
    print(messages)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=function_descriptions,
            function_call="auto",
            temperature = 0.1)

        print(response["choices"][0]["message"])
    except:
        time.sleep(20)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=function_descriptions,
            function_call="auto",
            temperature = 0.1)

        print(response)
    while response["choices"][0]["finish_reason"] == "function_call":
        
        function_response = function_call(response,id_)
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
        #print(messages)
        while True:
            try:
                response = openai.ChatCompletion.create( 
                    model="gpt-3.5-turbo-0613",
                    messages=messages,
                    functions = function_descriptions,
                    function_call="auto",
                    temperature = 0.9
                )
                break
            except openai.error.RateLimitError:
                print('Maximum rate limit reached wait 20s')
                time.sleep(20)
                
            print(response["choices"][0]["message"])
    return response

