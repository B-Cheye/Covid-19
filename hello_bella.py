# Pathway to dashboard json file
import json
import requests
import pprint
import pandas as pd
data = json.loads(requests.get("https://pomber.github.io/covid19/timeseries.json").text)
# Open and view file
#with open(data) as f:
#  json_data = json.load(f)
country_names = list(data.keys())
column_names = []
column_names.append('country')
json_keys = list(data['Afghanistan'][0].keys())
column_names.extend(json_keys)
data_pd = pd.DataFrame(columns = column_names)
date_list = []
confirmed_list = []
deaths_list = []
recovered_list = []
country_list = []
for country in country_names:
  for item in list(data[country]):
    country_list.append(country)
    date_list.append(item['date'])
    confirmed_list.append(item['confirmed'])
    deaths_list.append(item['deaths'])
    recovered_list.append(item['recovered'])
data_pd['country'] = country_list
data_pd['date'] = date_list
data_pd['confirmed'] = confirmed_list
data_pd['deaths'] = deaths_list
data_pd['recovered'] = recovered_list
print(data_pd.tail())