#1
print("\n#1 if\n")
x,y,z=10,20,5
if x > y:
	print("x > y")
else:
	print("x <= y")

#2
print("\n#2elif")
x,y,z=10,20,5
if x > y:
	print("x > y")
elif x > z:
	print("x > z")

#3
print("\n#3while")
x=3
while x > 0:
	print("x =",x)
	x-=1