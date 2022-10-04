# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:31:47 2022

@author: shao'dong'hao
"""
import json
import pandas as pd
from pandas.core.frame import DataFrame
papers=[]
applicants=[]
endlist=[]
#file= open('D:/工作文件新/云端互联/云端互联/中信所/信息中心项目/样例与字典/方法中心/美国专利库-样例数据/美国专利库-样例数据.json', 'r',encoding='utf-8')
#with open('D:/工作文件新/云端互联/云端互联/中信所/信息中心项目/样例与字典/方法中心/美国专利库-样例数据/美国专利库-样例数据.json', 'r',encoding='utf-8')
with open('D:/工作文件新/云端互联/云端互联/中信所/信息中心项目/样例与字典/方法中心/美国专利库-样例数据/美国专利库-样例数据.json', 'r',encoding='utf-8') as file:
    line = file.readline()
    counts = 1
    while line:
        if counts >= 500:
            break
        line = file.readline()
        dic = json.loads(line)
        papers.append(dic)
        counts += 1
ls=pd.DataFrame(papers)

ls.info()

for line in file.readlines():
    dic = json.loads(line)
    papers.append(dic)
ls=pd.DataFrame(papers)
type(file)
