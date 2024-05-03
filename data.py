print('We are collecting the Data..')


import pandas as pd
import numpy as np


d = { 'Id' : [101,102,103],
     "Age" : [20,22,11]}

df = pd.DataFrame(d)

print(df)