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
u='https://iqtestprep.com/nfl-wonderlic-scores/'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup('tr')
del tag[0]
name=[]
score=[]
pos=[]
for i in tag:
    i=i.get_text()
    j=re.findall('[A-Za-z]+',i)
    k=re.findall('[0-9]+',i)
    n=''
    for l in range(0,len(j)-1):
        n=n+j[l]+' '
    n=n.rstrip()
    if n=='Robert Griffin III':
        name.append('Robert Griffin')
    else:
        name.append(n)
    pos.append(j[len(j)-1])
    score.append(int(k[0]))
data={'Name':name,'Wonderlic Score':score,'Position':pos}
data=pd.DataFrame(data)
pd.set_option('display.max_rows',700)
data2=data[data['Position']=='QB']
col=['Name','Wonderlic Score']
data2=data2[col]
data2.drop_duplicates(subset="Name",keep='last',inplace=True)
data2=data2.sort_values(by='Wonderlic Score',ascending=True)
data2=data2.reset_index(drop=True)
data2.index=np.arange(1,len(data2)+1)
u='https://www.pro-football-reference.com/awards/super-bowl-mvp-award.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup('td')
tag2=[]
for temp in range(0,len(tag)):
    if tag[temp].get('data-stat')!='league_id' and tag[temp].get('data-stat')!='team':
        tag2.append(tag[temp].get_text())
data3={}
for i in tag2:
    if i in name:
        if i not in data3:
            data3.update({i:1})
        elif i in data3:
            data3[i]+=1
data2.insert(2,'SB MVP(s)',0)
temp=1
for i in data2['Name']:
    if i in data3:
        data2.loc[temp,'SB MVP(s)']=data3[i]
    temp+=1
u='https://www.pro-football-reference.com/awards/ap-nfl-mvp-award.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup('td')
tag3=[]
for temp in range(0,len(tag)):
    if tag[temp].get('data-stat')!='league_id' and tag[temp].get('data-stat')!='team':
        tag3.append(tag[temp].get_text())
data3={}
for i in tag3:
    if i in name:
        if i not in data3:
            data3.update({i:1})
        elif i in data3:
            data3[i]+=1
data2.insert(3,'MVP(s)',0)
temp=1
for i in data2['Name']:
    if i in data3:
        data2.loc[temp,'MVP(s)']=data3[i]
    temp+=1
u='https://www.pro-football-reference.com/probowl/'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup.find_all('table')[0]
tag3=[]
for row in tag.find_all('tr'):
    for row1 in row.find_all('td'):
        for row2 in row1.find_all('a'):
            if 'Pro Bowl Roster' not in row2.get_text():
                tag3.append(row2.get_text())
data3={}
for i in tag3:
    if i in name:
        if i not in data3:
            data3.update({i:1})
        elif i in data3:
            data3[i]+=1
data2.insert(4,'Pro Bowl MVP(s)',0)
temp=1
for i in data2['Name']:
    if i in data3:
        data2.loc[temp,'Pro Bowl MVP(s)']=data3[i]
    temp+=1
u='https://www.pro-football-reference.com/awards/ap-offensive-rookie-of-the-year-award.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup('td')
tag3=[]
for temp in range(0,len(tag)):
    if tag[temp].get('data-stat')!='league_id' and tag[temp].get('data-stat')!='team':
        tag3.append(tag[temp].get_text())
data3={}
for i in tag3:
    if i in name:
        if i not in data3:
            data3.update({i:1})
        elif i in data3:
            data3[i]+=1
data2.insert(5,'OPOY',0)
temp=1
for i in data2['Name']:
    if i in data3:
        data2.loc[temp,'OPOY']=data3[i]
    temp+=1
u='https://www.pro-football-reference.com/leaders/pass_yds_career.htm'
f=urllib.request.urlopen(u).read()
soup=BeautifulSoup(f,'html.parser')
tag=soup.find_all('table')[0]
data3={}
data4={}
for row in tag.find_all('tr'):
    if len(row.find_all('td'))>0:
        i=row.find_all('td')[0].get_text().replace('+','')
        j=int(row.find_all('td')[1].get_text().replace(',',''))
        k=row.find_all('td')[2].get_text().split('-')
        l=int(k[1])-int(k[0])+1
        data3[i]=j
        data4[i]=l
data2.insert(6,'Passing Yards',0)
data2.insert(7,'Seasons Played',0)
temp=1
for i in data2['Name']:
    if i in data3:
        data2.loc[temp,'Passing Yards']=data3[i]
    if i in data4:
        data2.loc[temp,'Seasons Played']=data4[i]
    temp+=1
data2.insert(8,'Success',0)
temp=1
for i in data2['Name']:
    v1=data2.loc[temp,'SB MVP(s)']
    v2=data2.loc[temp,'MVP(s)']
    v3=data2.loc[temp,'Pro Bowl MVP(s)']
    v4=data2.loc[temp,'OPOY']
    v5=data2.loc[temp,'Passing Yards']
    v6=data2.loc[temp,'Seasons Played']
    if v6!=0:
        data2.loc[temp,'Success']=round((1.3*v1)+(2*v2)+(0.4*v3)+(0.15*v4)+(0.0035*v5/v6),3)
    else:
        data2.loc[temp,'Success']=round((1.3*v1)+(2*v2)+(0.4*v3)+(0.15*v4),3)
    temp+=1
print(data2.describe())
print(stats.describe(data2['Wonderlic Score']))
data2.to_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw.csv',index=False,header=True)
