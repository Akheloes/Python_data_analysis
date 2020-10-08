import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os
from local_setting import dataFilePath

sales = pd.read_csv(dataFilePath, parse_dates=['Date'])

heades = sales.head()

print(heades)