# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 20:47:12 2021

@author: zhangyuanqi
"""

import pandas as pd 

#数据加载
df=pd.read_csv('car_complain.csv')

#拆分problem类型至多个字段
df=df.drop('problem',1).join(df.problem.str.get_dummies(','))
df=df.replace('一汽大众','一汽-大众')
tags = df.columns[7:]

#计算每个车型总投诉数量
result1=df.groupby(['brand','car_model'])[tags].agg(['sum'])
result1['车型总投诉数']=result1.sum(axis=1)
result1=result1['车型总投诉数']

#计算每个品牌车型数量
result2=result1.groupby(['brand']).agg(['count'])
result2['车型数']=result2['count']
result2=result2['车型数']

#计算每个品牌总投诉量
result3=result1.groupby(['brand']).agg(['sum'])
result3['品牌总投诉数']=result3['sum']
result3=result3['品牌总投诉数']

#打印各车型投诉量并排序
result1=result1.reset_index()
result1=result1.fillna('ffill')
result1=result1.sort_values(by='车型总投诉数',ascending=False)
print('各车型投诉情况：')
print(result1)

#打印各品牌平均车型投诉并排序
result=pd.merge(result2,result3,left_index=True,right_index=True,how='left')
result['平均车型投诉']=result['品牌总投诉数']/result['车型数']
result['平均车型投诉']=result['平均车型投诉'].round(2)
result=result.sort_values('平均车型投诉',ascending=False)
print('各品牌平均车型投诉情况：')
print(result)

