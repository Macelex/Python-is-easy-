print()
Title =    "      Pyhhon Is Easy !       "
SubTitle = "  Homework Assignment - 3  " 
print(Title)
print(SubTitle)
print()
def Equality(a,b,c):
	if a==b==c:
		print(True,": a=b=c", "i.e.",a,"=",b,"=",c)
	elif a==b:
		print(True,": a=b", "i.e.",a,"=",b)
	elif b==c:
		print(True,": b=c", "i.e.",b,"=",c)
	elif c==a:
		print(True,": c=a", "i.e.",c,"=",a)
	else:
		print(False,": No number is equal to other number", "as a ≠ b ≠ c","i.e.",a,"≠",b,"≠",c)
	pass

Equality(2,43,4)

