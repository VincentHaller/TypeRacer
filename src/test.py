#%%
import numpy as np
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

l_num = []
l_per = []
#%%



req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

html_race_num = soup.find_all('div', 'profileTableHeaderUniverse')
html_race_per = soup.find_all('div', 'profileTableHeaderRaces')

for num in html_race_num:
	l_num.append(float(
		num.text
		.replace('\n', '')
		.replace(' ', '')
	))
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
for date in html_race_date:
	print(
		date.text
		.replace('\n', '')
		.replace(' ', '')
		)
# %%
date.text.replace('\n', '').replace(' ', '')

# %%
