

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from datetime import datetime


now = datetime(2011,11,29)

ts = Series(np.random.randn(20),index = pd.date_range('1/15/2000',periods = 20,freq = '4d'))
print(ts,'\n')

print(ts.resample('M'))