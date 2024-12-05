#%%
import numpy as np 
import matplotlib.pyplot as plt
from src.scrapper_function import load_typeracer_results
import cProfile


#%%

np_data = load_typeracer_results()
# %%
cProfile.run('load_typeracer_results()', sort='tottime')
# %%
plt.scatter(np_data[:, 0], np_data[:,1], alpha = 0.5)
plt.title('WPM')
plt.show()

plt.plot(np_data[:, 0], np_data[:, 2])
plt.title('Accuracy')
plt.show()

plt.scatter(np_data[:, 2], np_data[:, 1])
plt.title("Accuracy vs Speed")
plt.show()
# %%
import pandas as pd
# %%
df = (
	pd.DataFrame(np_data, columns=["Race", "WPM", "Accuracy", "date"])
	.assign(date = lambda df: (
		pd.to_datetime('1970-01-01')
		+ df['date'].apply(lambda x: pd.Timedelta(x, 'D'))
	))
	.set_index("date")
	.sort_index()
	.rolling('5d')
	.mean()
	.dropna()
	.drop(columns=['Race'])
	.loc["2024":]
	.reset_index()
)

# %%
df.plot.scatter(x='date', y='WPM', alpha = 0.5)
# %%
np_data
# %%
pd.to_datetime('1970-01-01') + pd.Timedelta(df['date'], 'D')
# %%
df['WPM']
# %%
# %%
df

# %%
df['date'].apply(lambda x: pd.Timedelta(x, 'D'))
# %%
