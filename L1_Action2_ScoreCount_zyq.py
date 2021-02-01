# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:39:50 2021

@author: zhangyuanqi
"""

import pandas as pd
from pandas import DataFrame 

data={'语文':[68,95,98,90,80],
      '数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'],columns=['语文','数学','英语'])
#创建统计表
statistics=pd.DataFrame(columns=['语文','数学','英语'])
statistics.loc['mean']=df.mean() #平均成绩
statistics.loc['min']=df.min() #最小成绩
statistics.loc['max']=df.max() #最大成绩
statistics.loc['var']=df.var() #方差
statistics.loc['std']=df.std() #标准差
print('成绩统计：')
print(statistics)
df['总成绩']=df.sum(axis=1) #总成绩
df=df.sort_values(by='总成绩',ascending=False) #排名
print('成绩排名：')
print(df)