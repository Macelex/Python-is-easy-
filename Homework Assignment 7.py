"""
Instead of converting each variable and value to a key and 
it's corresponding value, I created a loop that will convert 
the inputs into key and values separately. 

"""

DirectoryMusic = {}
rangeOfDirectory = int(input("How many keys would you like to enter ? : "))

"""
This code has been used to check how many values a person
would like to enter.....

"""
rangeOfDirectory2 = 0

"""
this code is used to create another variable so that when
this and the above variable is equal, we can brewk the loopm

"""
if rangeOfDirectory2 != rangeOfDirectory:
	while rangeOfDirectory != rangeOfDirectory2:
		keyinput = input("Pls enter a key : ")
		valueinput = input("Pls enter a value : ")
		DirectoryMusic.update({keyinput:valueinput})
		rangeOfDirectory2 += 1
		if rangeOfDirectory2 == rangeOfDirectory:
				for k,v in DirectoryMusic.items():
					print(str(k) + '- ' + str(v))
					"""
					To print the key input and value simultaneously,
					side by side, the above code has been used.....		

					"""
					print(" Thank You !!")



	

	


	





