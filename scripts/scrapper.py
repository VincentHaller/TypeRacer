#%% Imports
import sys
sys.path.append('..')

import numpy as np
import pandas as pd
import json
import requests

from bs4 import BeautifulSoup

# %%
type_url = json.load(open("config/url.json"))

#%%
url = f"{type_url['url_start']}{type_url['user']}{type_url['url_end']}"

r = requests.get(url)
# %%
soup = BeautifulSoup(r.content, 'html.parser')
# %%
print(soup.title)
# %%
s = soup.find('div', class_='profileTableHeaderUniverse')
# %%
lines =s.find_all_next('a')
# %%
for line in lines:
	print(line.text)
# %%
print(r.content)
# %%
print(str(r.content))
# %%
s.find_all_next('a')
# %%

lines[0].__str__.contains('details')
# %%
soup.find_all('a')[0].text
# %%
soup.find_all('div','profileTableHeaderRaces' )
# %%

race_number = soup.find_all('div', 'profileTableHeaderUniverse')

# %%
for num in race_number:
	print(int(num.text.translate({'\n':None, ' ':None})))
# %%
