name = input("Enter a name ==> ")
if name.endswith("Gumby"):
 if name.startswith("Mr."):
  print("嗨，Gumby先生")
 elif name.startswith("Mrs."):
  print("嗨，Gumby女士")
 else:
  print("您好，Gumby")
else:
 print("我不認得你，sorry")
