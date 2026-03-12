name =input("請輸入你的名字:")
dozens=int(input("請輸入幾打:"))
people=int(input("將分送給多少人:"))

all=dozens*12#總共有幾顆蛋
average=all//people#平均每人分到多少顆
remain=all%people#剩下多少顆
print("{}同學，你總共有{}顆蛋，平均每人分到{}顆，剩下{}顆。".format(name,all,average,remain))