def simpleGeneratorFun(): 
	yield "first yield"
	yield "second yield"
	yield "third yield"

# Driver code to check above generator function 
a = [1,2,3,4,5,6]
for x in range(6): 
	for value in simpleGeneratorFun():
		print(value)