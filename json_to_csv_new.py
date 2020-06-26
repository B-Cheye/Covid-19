import json
import pandas as pd 
from pandas.io.json import json_normalize
file_name = 'https://pomber.github.io/covid19/timeseries.json'
#with open('https://pomber.github.io/covid19/timeseries.json') as f:
#    d = json.load(f)
file_name = json.load(file_name)
#normalized_json = json_normalize(file_name)
print(file_name)
