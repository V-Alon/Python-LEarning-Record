import numpy as np
import pandas as pd

a=pd.DataFrame(np.arange(12).reshape((4, 3)),columns=['A','B','C'],index=[1,2,3,4])
print(a)


d1={'name':['11','22'],'age':['11','22'],'tel':['11','22']}
e1=pd.DataFrame(d1)
print(e1)

d2=[{'name':'111','age':'11','tel':'100'},{'name':'222','tel':'101'},{'name':'333','age':'33'}]
e2=pd.DataFrame(d2)
print(e2)