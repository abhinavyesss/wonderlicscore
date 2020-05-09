import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import numpy as np
from scipy import stats
import re
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
data2=pd.read_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw2.csv')
u='https://www.pro-football-reference.com/leaders/pass_int_career.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup.find_all('table')[0]
tag3=[]
tag4=[]
for row in tag.find_all('tr'):
    for row1 in row.find_all('td'):
        if row1.get('data-stat')=='player':
            tag3.append(row1.get_text().replace('+',''))
        elif row1.get('data-stat')=='pass_int':
            tag4.append(row1.get_text())
dict=dict.fromkeys(tag3,0)
temp=0
for i in dict:
    dict[i]=int(tag4[temp])
    temp+=1
temp=0
for i in data2['Name']:
    if i in dict:
        data2.loc[temp,'Interceptions']=dict[i]
    temp+=1
u='https://www.pro-football-reference.com/leaders/pass_td_career.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup.find_all('table')[0]
tag3=[]
tag4=[]
for row in tag.find_all('tr'):
    for row1 in row.find_all('td'):
        if row1.get('data-stat')=='player':
            tag3.append(row1.get_text().replace('+',''))
        elif row1.get('data-stat')=='pass_td':
            tag4.append(row1.get_text())
dict=dict.fromkeys(tag3,0)
temp=0
for i in dict:
    dict[i]=int(tag4[temp])
    temp+=1
temp=0
for i in data2['Name']:
    if i in dict:
        data2.loc[temp,'Touchdowns']=dict[i]
    temp+=1
u='https://www.pro-football-reference.com/leaders/pick_six_career.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup.find_all('table')[0]
tag3=[]
tag4=[]
for row in tag.find_all('tr'):
    for row1 in row.find_all('td'):
        if row1.get('data-stat')=='player':
            tag3.append(row1.get_text().replace('+',''))
        elif row1.get('data-stat')=='pick_six':
            tag4.append(row1.get_text())
dict=dict.fromkeys(tag3,0)
temp=0
for i in dict:
    dict[i]=int(tag4[temp])
    temp+=1
temp=0
for i in data2['Name']:
    if i in dict:
        data2.loc[temp,'Pick 6s']=dict[i]
    temp+=1
data2.to_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw2.csv',index=False,header=True)
