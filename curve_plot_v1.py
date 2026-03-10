#Program: curve_plot_v1.py (Report comments/bugs to chikh@yuntech.edu.tw)
#Function: 繪製f(x)=x*log10(1+x**2)exp(-x**2)之函數圖形
#Note: 繪圖指令參見 https://matplotlib.org/stable/tutorials/introductory/pyplot.html

import math 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#-------------------------------------------------------------------#
#創建(x,f(x))對應若干位置點存於串列，融合http://bit.ly/2Inq6d9介紹的寫法
N = 10000 		#區間內分為10000點
xIntvLen = 6	#interval length: 區間[-3,3]寬度
x = [-3+xIntvLen*(p/N) for p in range(N)] #趕緊筆記起來
fx = []	
for i in range(N): #計算每一x所對應的f(x)值，儲存於fy串列
	fx.append(x[i]*math.log10(1+x[i]*x[i])*math.exp(-x[i]*x[i]))
#-------------------------------------------------------------------#

plt.plot(x,fx,linewidth=0.5)
plt.xlabel('x'); #plt.ylabel('y')
#chineseFont = FontProperties('SimHei') 
chineseFont = FontProperties(fname = 'C:\\Windows\\Fonts\\msjh.ttc') #FontProperties(fname = 'C:\\Windows\\Fonts\\DFW_PD7.TTC')
plt.xlabel(u"x軸",fontproperties = chineseFont, fontsize=20) #參考http://bit.ly/2p46ggw
plt.show()
