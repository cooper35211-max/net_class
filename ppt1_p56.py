#1
print('\n#1')
zdict = {}	#創建空字典
zdict['w1'] = 'hello'
zdict['w2'] = 'mit.edu'
zdict['w3'] = 10
print('zdict,',zdict)
print("zdict.items() = ",zdict.items())

print("字典的鍵值",zdict.keys())

for x in zdict.keys():	#for迴圈與if陳述的寫將在後面的進度有更多講解
	print("Key =",x,"\tValue =",zdict[x])
	if x == 'w3':
		zdict[x] += 20	
print('zdict,',zdict,'; zdict[\'w3\'] =',zdict['w3'])

'''
for key,val in zdict.items():
	print("Key =",key,"type = ",type(key),"\tValue =",val)
	if key == 'w3':
		zdict[key] += 20
'''

#2
print('\n#2')
vdict={'url1':'TopQuant.vip'
       ,'url2':'www.TopQuant.vip'
       ,'url3':'mit.edu'}
print('vdict,',vdict)

#3
print('\n#3')
s2=zdict['w1']; print('s2,',s2)
s3=vdict['url2']; print('s3,',s3)