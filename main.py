import pandas as pd 
import json
import pprint
from pandas.io.json import json_normalize
file_name = 'https://pomber.github.io/covid19/timeseries.json'
data = pd.read_json(file_name)
covid_json = data.to_json()
codid_json_new = json.loads(covid_json)
#normalized_json = json_normalize(read_json_here)
#afg = codid_json_new['Afghanistan']
#print(type(codid_json_new))
#df = pd.DataFrame(codid_json_new).T
pprint.pprint(covid_json)
