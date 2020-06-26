import requests
import json
import pprint
import pandas as pd 
response = json.loads(requests.get("https://pomber.github.io/covid19/timeseries.json").text)
#print(type(response))
df = pd.DataFrame.from_dict(response, orient='columns')

def unnest_dict(nested_dict):
    for key,value in nested_dict.items():
        if type(value) is list:
            for d in value:
                unnest_dict(d)            
        else:
            print(key,value)

print(unnest_dict(response))