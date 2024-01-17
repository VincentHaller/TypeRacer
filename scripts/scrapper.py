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
plt.plot(np_data[:, 0], np_data[:,1])
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
	pd.DataFrame(np_data, columns=["Race", "WPM", "Accuracy"])
	.set_index("Race")
	.sort_index()
	.rolling(10)
	.mean()
)

# %%
df.plot()
# %%
