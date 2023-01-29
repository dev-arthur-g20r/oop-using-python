class Person:
	# `Person` is the base class of child class `Employee`.
	# Constructor
	def __init__(self, firstName, lastName):
		self.firstName = firstName # Property pertaining to first name.
		self.lastName = lastName # Property pertaining to last name.

	# Method
	def greet(self):
		print(f"Hello! I am {self.firstName} {self.lastName}.")
		# Using f-strings is one way to use string interpolation.

	# Property - adjective of the class
	# Method - verb of the class
	# Object - Instance of a class

arthur = Person("Arthur", "Ramos") # Object - Instance of a class
arthur.greet()

# Inheritance (`Employee` inherits from `Person`.)
class Employee(Person):
	def __init__(self, firstName, lastName, position):
		super().__init__(firstName, lastName)
		self.position = position

	def greet(self, salary):
		print(f"Good day! I am {self.firstName} {self.lastName} and I am a {self.position}. I earn ${salary} per month.")

louise = Employee("Louise John", "Soria", "Graphics Designer")
louise.greet(15000)

katrina = Employee("Katrina Mae", "De Leon", "Leader")
katrina.greet(20000)