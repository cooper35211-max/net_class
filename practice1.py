#1
dss=" #hello Pyqt6,,"
print("去除空格與特殊符號")

#s1=dss.strip().rstrip(",")
print("s1=",dss)
s1=dss.strip().lstrip("#").rstrip(",")
print("s1=",s1)

#2
print("\n#2字串連結")
#s2="#".join(["a",".","c"]);print("s2",s2)#輸出 a#.#c
s2=dss.join(["a",".","c"]);
print("s2=",s2)#輸出 a #hello Pyqt6,, . #hello Pyqt6,, c
s3="s3"
s3+="xx"
print("s3=",s3)

#3
print("\n#3 查找字元")
css="abclc2c3"
pi=css.find("c3")
print("pi=",pi)#-1表示沒有找到

#4
print("\n#4 字串比較")
print(s1>s2)
print(s1==s2)
print(s1<s2)