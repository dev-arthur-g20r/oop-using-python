class Calculator:
	# `self` refers to class' own instance.
	def __init__(self, firstNumber, secondNumber):
		self.firstNumber = firstNumber
		self.secondNumber = secondNumber

	def add(self):
		return self.firstNumber + self.secondNumber

	def subtract(self):
		return self.firstNumber - self.secondNumber

	def multiply(self):
		return self.firstNumber * self.secondNumber

	def divide(self):
		return self.firstNumber / self.secondNumber

arithmeticOperators = ["+", "-", "*", "/"]
firstNumber = float(input("First Number = "))
arithmeticOperator = input("Operator (+ - * /): ").strip()
secondNumber = float(input("Second Number = "))
calculator = Calculator(firstNumber, secondNumber)

result = "Invalid operator! Please try again."

if (arithmeticOperator in arithmeticOperators):
	if (arithmeticOperator == "+"):
		sumResult = calculator.add()
		result = f"{sumResult}"
	elif (arithmeticOperator == "-"):
		difference = calculator.subtract()
		result = f"{difference}"
	elif (arithmeticOperator == "*"):
		product = calculator.multiply()
		result = f"{product}"
	elif (arithmeticOperator == "/"):
		quotient = calculator.divide()
		result = f"{quotient}"

print(result)