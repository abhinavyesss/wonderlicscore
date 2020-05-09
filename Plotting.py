import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
data2=pd.read_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Scores_Raw3.csv')
mvpdata=pd.read_csv(r'C:\Users\ABHINAV\Desktop\MYWork\Data Science and Machine Learning Specializations\Python Programs\NFL Wonderlic\Averages.csv')
topdata=data2.sort_values(by='Success',ascending=False)
topdata=topdata[:12]
sns.set_color_codes()
plt.figure(figsize=(10,10)).suptitle('Plots I')
sns.scatterplot(x=data2['Wonderlic Score'],y=data2['Success'],data=data2,color='blue')
sns.scatterplot(x=topdata['Wonderlic Score'],y=topdata['Success'],data=topdata,color='green')
for i in range(0,len(topdata['Name'].tolist())):
    txt=topdata['Name'].tolist()[i]
    plt.annotate(txt,(topdata['Wonderlic Score'].tolist()[i],topdata['Success'].tolist()[i]))
plt.figure(figsize=(10,10)).suptitle('Plots II')
plt.subplot(2,2,1)
sns.distplot(data2['Wonderlic Score'],kde=False,color='purple')
plt.subplot(2,2,3)
sns.distplot(data2['Wonderlic Score'],hist=False,kde=True,kde_kws={'shade':True,'linewidth':3},color='purple')
plt.subplot(2,2,2)
sns.barplot(x=mvpdata['Score Ranges'],y=mvpdata['MVP(s)'],data=mvpdata)
plt.subplot(2,2,4)
sns.barplot(x=mvpdata['Score Ranges'],y=mvpdata['SB MVP(s)'],data=mvpdata)
plt.figure(figsize=(10,10)).suptitle('Plots III')
plt.subplot(2,2,1)
sns.barplot(x=mvpdata['Score Ranges'],y=mvpdata['AvgTD'],data=mvpdata)
plt.subplot(2,2,3)
sns.barplot(x=mvpdata['Score Ranges'],y=mvpdata['AvgPass'],data=mvpdata)
plt.subplot(2,2,2)
sns.barplot(x=mvpdata['Score Ranges'],y=mvpdata['AvgInt'],data=mvpdata)
plt.subplot(2,2,4)
sns.barplot(x=mvpdata['Score Ranges'],y=mvpdata['AvgTD']-mvpdata['AvgInt'],data=mvpdata).set_ylabel('TD - Interception')
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(222,projection='3d')
xpos=[0,10,20,30,40]
ypos=mvpdata['Number of Players'].tolist()
zpos=[0,0,0,0,0]
dx=np.ones(5)*10
dy=np.ones(5)*10
dz=mvpdata['Total Passing Yards'].tolist()
ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='crimson')
ax.set_xlabel('Score Ranges')
ax.set_ylabel('No. of Players')
ax.set_zlabel('Total Passing Yards')
ax=fig.add_subplot(221,projection='3d')
xpos=[0,10,20,30,40]
ypos=mvpdata['Number of Players'].tolist()
zpos=[0,0,0,0,0]
dx=np.ones(5)*10
dy=np.ones(5)*10
dz=mvpdata['Total Touchdowns'].tolist()
ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='maroon')
ax.set_xlabel('Score Ranges')
ax.set_ylabel('No. of Players')
ax.set_zlabel('Total Touchdowns')
ax=fig.add_subplot(223,projection='3d')
xpos=[0,10,20,30,40]
ypos=mvpdata['Number of Players'].tolist()
zpos=[0,0,0,0,0]
dx=np.ones(5)*10
dy=np.ones(5)*10
dz=mvpdata['Total Interceptions'].tolist()
ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='lightgreen')
ax.set_xlabel('Score Ranges')
ax.set_ylabel('No. of Players')
ax.set_zlabel('Total Interceptions')
plt.show()
print(data2.describe())
print(stats.describe(data2['Wonderlic Score']))
