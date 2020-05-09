import pandas as pd
import webbrowser
import math
data2=pd.read_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw2.csv')
temp=0
l=[]
pd.set_option('display.max_rows',700)
for i in data2['Name']:
    if int(data2.loc[temp,'Passer Rating'])==0:
        i=i.replace(' ','_')
        l.append(i)
    temp+=1
temp=25
for i in l:
    s='https://en.wikipedia.org/wiki/'+l
    webbrowser.open(s)
temp=0
l=[]
for i in data2['Name']:
    if int(data2.loc[temp,'Passing Yards'])<1500:
        l.append(temp)
    temp+=1
if l==[]:
    pass
else:
    print('Done!')
data2=data2.drop(l)
'''
temp=0
for i in data2['Name']:
    v1=int(data2.loc[temp,'SB MVP(s)'])
    v2=int(data2.loc[temp,'MVP(s)'])
    v3=int(data2.loc[temp,'Pro Bowl MVP(s)'])
    v4=int(data2.loc[temp,'OPOY'])
    v5=int(data2.loc[temp,'Passing Yards'])
    v6=int(data2.loc[temp,'Seasons Played'])
    v7=int(data2.loc[temp,'Touchdowns'])
    v8=int(data2.loc[temp,'Interceptions'])
    v9=int(data2.loc[temp,'Pick 6s'])
    v10=int(data2.loc[temp,'Completion %'])
    v11=int(data2.loc[temp,'Passer Rating'])
    data2.loc[temp,'Success']=(1.8*v1)+(2*v2)+(0.3*v3)+(0.1*v4)+(0.0035*v5/v6)+((0.11*v7-0.101*v8)/v6)-(0.02*v9/v6)+(math.exp(v6*0.0081)*(0.0018*v11+0.0001*v10))
    data2.loc[temp,'Success']=round(data2.loc[temp,'Success'],3)
    temp+=1'''
print(data2.describe())
data2.to_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw3.csv',index=False,header=True)
