#! /bin/python3

#print string
#print("Hello world.")

#new line
#print("\n")

#print second string
#print("It's so lonely here...")

#functions
#print("This function is about to execute.\n")
#def who_am_i():
#    name = "Ivan"
#    age = 34
#    print("My name is " + name + " and I am " + str(age) + " years old.")

#who_am_i()

#function with params
#def who_are_you(name, age):

#    print("Your name is " + name + " and your age is " + str(age) + " years old.")

#who_are_you("David", 32)

#lists
#friends = ["Joey", "Monica", "Chandler", "Ross", "Rachel", "Phoebe"]

#print(friends[0])
#print(friends[0:2])

#for loop
#food = ["pizza", "burger", "fries", "kebab", "shawarma"]

#for x in food:
#    print(x)

#i = 0
#while i < 5:
#    print(food[i])
#    i += 1

#trick to fill buffer
#buffer = "A" * 10

#print(buffer)

student = {'name': 'John', 'age': 32, 'courses': ['Math', 'CompSci']}

print(student)

print("\n")

print(student['name'])

print("\n")

print(student.get('courses'))

print("\n")

print(student.get('phone'))

print(student.get('height', 'Not Found'))

student['phone'] = '555-5555'

print(student)

del student['age']

print(student)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)
    
