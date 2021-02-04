# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:31:55 2021

@author: ZhangYuanqi
"""

import pandas as pd
from pandas import DataFrame 

data={'语文':[68,95,98,90,80],
      '数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
print(df.count())
print(df.min())
print(df.max())
print(df.mean())
print(df.var())
print(df.std())
#在df中添加列‘总和’并计算
df["总和"] =df.apply(lambda x:x.sum(),axis =1)
#按总和排列
df=df.sort_values('总和', ascending=False)              
print(df)

