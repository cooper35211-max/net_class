#Program: curve_plot_v2.py (Report bugs/comments to chikh@yuntech.edu.tw)
#Function: 繪製f(x)=x*log(1+x**2)*exp(-x**2)之函數圖形
#Note: 繪圖指令參見 https://matplotlib.org/tutorials/introductory/pyplot.html

import math 
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,1000)	#產生-3~3之間的數字陣列，內有1000個等距點
fx = np.array(list(map(lambda t: t*math.log(1+t*t)*math.exp(-t*t), x)))
fig, ax = plt.subplots()	#取得圖與座標軸之結構資訊
plt.plot(x,fx,linewidth=0.5)#linewidth設定線粗細
ax.axhline(y=0,color="black",linewidth=0.5,alpha=0.5)#繪x軸，alpha調淡
ax.axvline(x=0,color="black",linewidth=0.5,alpha=0.5)#繪y軸
plt.title(r"$f(x) = x\cdot ln(1+x^2)e^{-x^2}$")	#加圖標題

x = np.linspace(0,2,100)
y = np.array(list(map(lambda t: t*math.log(1+t*t)*math.exp(-t*t), x)))
plt.fill_between(x,0,y,color="red",alpha=0.1)	#(x,0)至(x,y)範圍內塗色

plt.show()
