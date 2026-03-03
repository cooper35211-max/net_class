#1
dss=" #hello Pyqt6,, "
print("去除空格與特殊符號")

#s1=dss.strip().rstrip(",")
print("s1=",dss)
s1=dss.strip().lstrip("#").rstrip(",")
print("s1=",s1)