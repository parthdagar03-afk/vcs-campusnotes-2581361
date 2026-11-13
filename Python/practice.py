import pandas as pd
import numpy as np

x1=pd.Series([10,20,30,40,50])
print("the list\n",x1)
x1.index=['a','b','c','d','e']
print("the list with index\n",x1)
print("marks of a =",x1['a'])
x1 = x1.drop('c')
print("after dropping c\n",x1)