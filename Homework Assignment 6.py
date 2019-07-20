print()
print()
Title = "            Homework Assignment - 6"
print(Title)
print()
print()
print("  Note = For checking how many number of rows & columns you want, follow the figure below --")
print()
print("                   Figure      Row Number")
print("                    | |            1")
print("                   -----           2")
print("                    | |            3")
print("                   -----           4")
print("                    | |            5")
print("  Column Number -  12345           ")
print()
print("  Therefore, if you want the figure above, the columns & rows would be 5. Adjust accordingly.")
print()
print("  Also, this is a Tic Tac Toe Board Constructor, so it only works when you give odd values to rows and columns")
print()
def BoardConstructor(rows, columns):
    for row in range(rows):
        if row%2 == 0:
            for column in range(1,columns+1):
                if column %2 == 1:
                    if column != columns:
                        print(" ",end="")
                    elif column == columns:
                        print(" ")
                elif column%2 == 0:
                    print("|",end= "")
        elif row%2 == 1:
            print("-"*columns)
BoardConstructor(5,7)
print()
BoardConstructor(7,7)
print()
BoardConstructor(9,9)
