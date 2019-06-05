Title = "Homework Assignment - 5"
print()
print(Title)
print()
print("All the numbers which are multiples of 3 and 5 both are replaced by 'FizzBuzz'")
print()
print("All the numbers which are multiples of 3 only are replaced by 'Fizz'")
print()
print("All the numbers which are multiples of 5 only are replaced by 'Buzz'")
print()
print("SEE BELOW !!")
print()

number = 0 
for number in range (101):
	if number%15 == 0:
		print("FizzBuzz")
		continue 
	elif number%3 == 0:
		print("Fizz")
		continue
	elif number%5 == 0:
		print("Buzz")
		continue
	else:
		print(number)
		continue
	number += 1