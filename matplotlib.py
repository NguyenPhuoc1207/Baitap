import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Bar chart
df = pd.read_csv("pandas.csv",index_col=(0))
#name=list(df['Name'])
#print(name)
fig, ax=plt.subplots()
ax.bar(df.index, df["Age"])
#ax.set_xticklabels(name)
ax.set_title('Bar Chart')
ax.set_ylabel('Tuổi')
ax.set_xlabel('Tên')
plt.show()

#Column chart:
gr = ['Tổ 1', 'Tổ 2', 'Tổ 3', 'Tổ 4']
nam = [20, 34, 30, 35]
nu = [25, 32, 34, 20]
x = np.arange(len(gr))  # the label locations
width = 0.35  #Độ rộng của cột
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, nam, width, label='Nam',color='b')
rects2 = ax.bar(x + width/2, nu, width, label='Nữ',color='tab:pink')
ax.set_ylabel('Điểm')
ax.set_title('Column Chart')
ax.set_xticks(x)
ax.set_xticklabels(gr)
ax.legend() #Thêm chú thích
plt.show()

#Line chart
df = pd.read_csv("pandas.csv",index_col=0)
fig, ax=plt.subplots()
ax.plot(df.index, df["Age"])
ax.set_ylabel('Tuổi')
ax.set_xlabel('Tên')
ax.set_title('Line Chart')
plt.show()

#Boxplot chart
df = pd.read_csv("pandas.csv", index_col=0)
fig, ax = plt.subplots()
ax.boxplot(df["Age"])
ax.set_ylabel('Tuổi')
ax.set_title('Boxplot Chart')
plt.show()