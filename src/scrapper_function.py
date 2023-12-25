#%% imports
import numpy as np
import json
import requests
import os
from bs4 import BeautifulSoup

		
# %% scrapper function
def load_typeracer_results(
		user:str=None,
		data_pos:str="data/", 
		json_config:str="config/url.json"
		):
	
	config = json.load(open(json_config))
	if not user:
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

	while True:
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

		min_found = min(l_num)

		if min_found <= min_search + 1:
			break

		href = soup.find_all('span')[-2].find('a').get('href')

		url = (f"""
			{config['url_0']}
			{href}
			"""
			.replace('\n', '')
			.replace('\t', '')
			)
	
	len_num = len(l_num)

	np_num = np.array(l_num).reshape([len_num, 1])
	np_per = np.array(l_per).reshape([len_num, 2])

	np_new = (
		np.concatenate([np_num, np_per], axis=1)
		[np.where(np_num[:,0] > min_search)]
		)

	if np_pre is not None:
		np_new = np.concatenate([np_new, np_pre], axis=0)

	np.savetxt(file_path, np_new, delimiter=',', newline='\n')

	return np_new


