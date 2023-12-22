#%%
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# %%
driver = webdriver.Firefox()
driver.get("http://www.python.org")
# %%
