import numpy as np
import pandas as pd

a=pd.DataFrame(np.arange(12).reshape((4, 3)),columns=['A','B','C'],index=[1,2,3,4])
print(a)