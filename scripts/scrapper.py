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
