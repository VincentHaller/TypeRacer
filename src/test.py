#%%
import numpy as np
import pandas as pd
import json
import requests
import os
from bs4 import BeautifulSoup
#%%


data_pos="data/", 
json_config="config/url.json"

config = json.load(open(json_config))

user = config['user']
file_path = f"{data_pos}{user}_typeracer_results.csv"

if os.path.exists(file_path):
	np_pre = np.genfromtxt(file_path, delimiter=',')
	min_search = np_pre[0, 0]
else:
	np_pre = None
	min_search = 0

url = (
	f"""
	{config['url_0']}
	{config['url_1']}
	{user}
	{config['url_end']}
	"""
	.replace('\n', '')
	.replace('\t', '')
)

min_found = np.inf

#%%
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

html_race_num = soup.find_all('div', 'profileTableHeaderUniverse')
html_race_per = soup.find_all('div', 'profileTableHeaderRaces')

l_num = []
for num in html_race_num:
	l_num.append(float(
		num.text
		.replace('\n', '')
		.replace(' ', '')
	))

l_per = []
for per in html_race_per:
	l_per.append(float(
		per.text
		.replace(' ', '')
		.replace('\n', '')
		.replace('%', '')
		.replace('WPM', '')
	))

	# min_found = min(l_num)
# %%
html_race_date = soup.find_all('div', 'profileTableHeaderDate')
# %%
l_date = []
for date in html_race_date:
	d = (
		date.text
		.replace('\n', '')
		.replace(',', '')
		.strip()
	)
	str_date = pd.to_datetime(d).date().strftime('%Y-%m-%d')
	l_date.append(str_date)

# %%
l_date
# %%
html_race_date

# %%
len(l_date)
# %%
np.array(l_date)

# %%
len(str_date)
# %%
float((pd.to_datetime(d) - pd.to_datetime('1970-01-01')).days)
# %%
pd.to_datetime('1970-01-01') + pd.Timedelta(19823.0, 'D')

# %%
