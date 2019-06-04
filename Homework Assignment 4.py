Title = "HomeWork Assignment - 4"
print()
Title =    "      Pyhhon Is Easy !       "
SubTitle = "  Homework Assignment - 4  " 
print(Title)
print(SubTitle)
print()
myUniqueList = []
def addUnique(myUniqueList, number):
     if number not in myUniqueList:
        myUniqueList.append(number)
        print(True , " : Hence, The 'Thing' has been added. See your list below !")
        print(myUniqueList)
     else:
     	print(False , " : Hence, your 'Thing' has not been added. See your list below !")
     	print(myUniqueList)
     return myUniqueList
addUnique(myUniqueList,"Python Is Really Easy")

