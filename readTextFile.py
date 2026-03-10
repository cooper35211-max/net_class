# Program: readTextFile.py
# Function: 提供二種方法，讀取輸入文檔並將內容顯示於螢幕
# Note: 參考	https://www.w3schools.com/python/python_file_open.asp 與 http://bit.ly/2U8ncOB

#f = open("inputText2.txt","r") #以純英數文字模式開啟檔案，以變數f儲存該檔案之結構
f = open("inputText2.txt","r",encoding="utf-8")	#文檔若含其他語系字元，加上"utf-8"編碼模式讀取較妥適
												#utf-8是甚麼意思？同學請查找網路看看

#--- 第一種方法 ---#
for x in f:	#使用for迴圈把f檔案內容逐字讀入x；無論任何字，有甚麼讀甚麼
  #print(x)	#把x一字一字打印出來
  print(x,end='') #請比較這個寫法與print(x)的差異在哪裡

"""
#--- 第二種方法 ---#
f.seek(0)	#檔案讀寫頭回轉至0位置，亦即檔案開頭位置
while True: 
	line = f.readline() #一次讀取一整行，讀入line變數儲存
	if line:	#line有內容(不為空)
		print(line,end='')
	else: 		#line為空，代表已讀不到東西了，則跳離迴圈
		break  
"""

f.close()	#關檔
