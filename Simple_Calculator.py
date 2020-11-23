#Simple Calculator , random try for if else

# This function performs additiion
def add(a, b):
   return a + b
# This function performs subtraction
def subtract(a, b):
   return a - b
# This function performs multiplication
def multiply(a, b):
   return a * b
# This function performs division
def divide(a, b):
	return a / b
#only options right now & only do with 2 numbers or values
print("Select an operation.")
print("+")
print("-")
print("*")
print("/")
# User input
choice = input("Enter valid symbol:")
A = int(input("Enter first num: "))
B = int(input("Enter second num: "))
if choice == '+':
   print(A,"+",B,"=", add(A,B))
elif choice == '-':
   print(A,"-",B,"=", subtract(A,B))
elif choice == '*':
   print(A,"*",B,"=", multiply(A,B))
elif choice == '/':
   print(A,"/",B,"=", divide(A,B))
else:
	print("Invalid input")