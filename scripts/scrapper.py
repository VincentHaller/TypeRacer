#%% Imports
import sys
sys.path.append('..')

import numpy as np
import pandas as pd
import json
import requests

import matplotlib.pyplot as plt 

from bs4 import BeautifulSoup

# %%
type_url = json.load(open("config/url.json"))

#%%
# url = f"{type_url['url_start']}{type_url['user']}{type_url['url_end']}"
url = "https://data.typeracer.com/pit/race_history?user=turbovince&universe=play&n=100&cursor=ClgKFgoJdGltZXN0YW1wEgkIiO6exLno9QISOmoTc350eXBlcmFjZXJkYXRhLWhyZHIjCxIKR2FtZVJlc3VsdCITX3RyOnR1cmJvdmluY2VfMTE2OAwYACAB&prevCursor=&startDate="

r = requests.get(url)
# %%
soup = BeautifulSoup(r.content, 'html.parser')
# %%
print(soup.title)

# %%
race_performance = soup.find_all('div','profileTableHeaderRaces' )
# %%

race_number = soup.find_all('div', 'profileTableHeaderUniverse')

l_race = []
l_perf = []
# %%
for race in race_number:
	l_race.append(int(race.text.translate({'\n':None, ' ':None})))
# %%
for perf in race_performance:
	l_perf.append(float(
		perf.text
		.replace(' ', '').replace('\n', '')
		.replace('WPM', '').replace('%', '')))
# %%
np_race = np.array(l_race).reshape(len(l_race), 1)
np_perf = np.array(l_perf).reshape([len(l_perf)//2, 2])
# %%


# %%
plt.scatter(np_perf[:,1], np_perf[:,0])
# %%

soup.find_all('span')

# %%
