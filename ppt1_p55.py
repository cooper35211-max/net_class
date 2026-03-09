#1
print('\n#1')
zlst = ('hello','PyQt6','.','com')
vlst = ('Top','Quant','.','vip')
print('zlst,',zlst)
print('vlst,',vlst)

#2
print('\n#2')
s2 = zlst[1:]; print('s2,',s2)
s3 = zlst[1:3]; print('s3,',s3)
s4 = vlst[:3]; print('s4,',s4)
#若加上 vlst[1] = 'Acer' 指令(修改vlst元素)，檢視是否可以？

#3
print('\n#3')
print('s2+s3,',s2+s3)
print('s3*2,',s3*2)