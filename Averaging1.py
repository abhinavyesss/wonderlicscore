import pandas as pd
import numpy as np
data2=pd.read_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw3.csv')
temp=0
dict={}
dict2={}
keylist=['0-9','10-19','20-29','30-39','40-50']
dict=dict.fromkeys(keylist,0)
for i in data2['MVP(s)']:
    if int(i)>0:
        if 0<=int(data2.loc[temp,'Wonderlic Score'])<10:
            dict['0-9']+=int(data2.loc[temp,'MVP(s)'])
        if 10<=int(data2.loc[temp,'Wonderlic Score'])<20:
            dict['10-19']+=int(data2.loc[temp,'MVP(s)'])
        if 20<=int(data2.loc[temp,'Wonderlic Score'])<30:
            dict['20-29']+=int(data2.loc[temp,'MVP(s)'])
        if 30<=int(data2.loc[temp,'Wonderlic Score'])<40:
            dict['30-39']+=int(data2.loc[temp,'MVP(s)'])
        if 40<=int(data2.loc[temp,'Wonderlic Score'])<=50:
            dict['40-50']+=int(data2.loc[temp,'MVP(s)'])
    temp+=1
i1=list(dict.values())
dict=dict.fromkeys(keylist,0)
temp=0
for i in data2['SB MVP(s)']:
    if int(i)>0:
        if 0<=int(data2.loc[temp,'Wonderlic Score'])<10:
            dict['0-9']+=int(data2.loc[temp,'SB MVP(s)'])
        if 10<=int(data2.loc[temp,'Wonderlic Score'])<20:
            dict['10-19']+=int(data2.loc[temp,'SB MVP(s)'])
        if 20<=int(data2.loc[temp,'Wonderlic Score'])<30:
            dict['20-29']+=int(data2.loc[temp,'SB MVP(s)'])
        if 30<=int(data2.loc[temp,'Wonderlic Score'])<40:
            dict['30-39']+=int(data2.loc[temp,'SB MVP(s)'])
        if 40<=int(data2.loc[temp,'Wonderlic Score'])<=50:
            dict['40-50']+=int(data2.loc[temp,'SB MVP(s)'])
    temp+=1
i2=list(dict.values())
dict=dict.fromkeys(keylist,0)
dict2=dict2.fromkeys(keylist,0)
temp=0
for i in data2['Passing Yards']:
    if int(i)>0:
        if 0<=int(data2.loc[temp,'Wonderlic Score'])<10:
            dict['0-9']+=int(data2.loc[temp,'Passing Yards'])
            dict2['0-9']+=1
        if 10<=int(data2.loc[temp,'Wonderlic Score'])<20:
            dict['10-19']+=int(data2.loc[temp,'Passing Yards'])
            dict2['10-19']+=1
        if 20<=int(data2.loc[temp,'Wonderlic Score'])<30:
            dict['20-29']+=int(data2.loc[temp,'Passing Yards'])
            dict2['20-29']+=1
        if 30<=int(data2.loc[temp,'Wonderlic Score'])<40:
            dict['30-39']+=int(data2.loc[temp,'Passing Yards'])
            dict2['30-39']+=1
        if 40<=int(data2.loc[temp,'Wonderlic Score'])<=50:
            dict['40-50']+=int(data2.loc[temp,'Passing Yards'])
            dict2['40-50']+=1
    temp+=1
i3=list(dict.values())
i4=list(dict2.values())
dict=dict.fromkeys(keylist,0)
temp=0
for i in data2['Touchdowns']:
    if int(i)>0:
        if 0<=int(data2.loc[temp,'Wonderlic Score'])<10:
            dict['0-9']+=int(data2.loc[temp,'Touchdowns'])
        if 10<=int(data2.loc[temp,'Wonderlic Score'])<20:
            dict['10-19']+=int(data2.loc[temp,'Touchdowns'])
        if 20<=int(data2.loc[temp,'Wonderlic Score'])<30:
            dict['20-29']+=int(data2.loc[temp,'Touchdowns'])
        if 30<=int(data2.loc[temp,'Wonderlic Score'])<40:
            dict['30-39']+=int(data2.loc[temp,'Touchdowns'])
        if 40<=int(data2.loc[temp,'Wonderlic Score'])<=50:
            dict['40-50']+=int(data2.loc[temp,'Touchdowns'])
    temp+=1
i5=list(dict.values())
dict=dict.fromkeys(keylist,0)
temp=0
for i in data2['Interceptions']:
    if int(i)>0:
        if 0<=int(data2.loc[temp,'Wonderlic Score'])<10:
            dict['0-9']+=int(data2.loc[temp,'Interceptions'])
        if 10<=int(data2.loc[temp,'Wonderlic Score'])<20:
            dict['10-19']+=int(data2.loc[temp,'Interceptions'])
        if 20<=int(data2.loc[temp,'Wonderlic Score'])<30:
            dict['20-29']+=int(data2.loc[temp,'Interceptions'])
        if 30<=int(data2.loc[temp,'Wonderlic Score'])<40:
            dict['30-39']+=int(data2.loc[temp,'Interceptions'])
        if 40<=int(data2.loc[temp,'Wonderlic Score'])<=50:
            dict['40-50']+=int(data2.loc[temp,'Interceptions'])
    temp+=1
i6=list(dict.values())
temp=0
mvpdata={'Score Ranges':keylist,'Number of Players':i4,'MVP(s)':i1,'SB MVP(s)':i2,'Total Passing Yards':i3,'Total Touchdowns':i5,'Total Interceptions':i6}
mvpdata=pd.DataFrame(mvpdata)
i7=np.zeros(len(mvpdata['Score Ranges'].tolist()))
i8=np.zeros(len(mvpdata['Score Ranges'].tolist()))
i9=np.zeros(len(mvpdata['Score Ranges'].tolist()))
for i in range(len(mvpdata['Score Ranges'].tolist())):
    if i4[i]==0:
        i7[i]=0
        i8[i]=0
        i9[i]=0
    else:
        i7[i]=i3[i]/i4[i]
        i8[i]=i5[i]/i4[i]
        i9[i]=i6[i]/i4[i]
mvpdata.insert(7,'AvgPass',i7)
mvpdata.insert(8,'AvgTD',i8)
mvpdata.insert(9,'AvgInt',i9)
print(mvpdata)
mvpdata.to_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Averages.csv',index=False,header=True)
