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
# %%
