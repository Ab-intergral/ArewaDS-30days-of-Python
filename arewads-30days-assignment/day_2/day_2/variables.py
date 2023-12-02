# Day 2: 30 Days of Python Programming
Exercise :level 1
first_name = 'Abubakar'
print(first_name)

last_name = 'Idi'
print(last_name)

full_name = first_name + ' ' + last_name
print(full_name)

country = 'Nigeria'
print(country)

city = 'Yola'
print(city)

age = 29
print(age)

year = 2023
print(year)

is_married = True
print(is_married)

is_true = True
print(is_true)

is_light_on = True
print(is_light_on)

address, education, job = 'Damilu Jimeta', 'B.Sc Mathematics', 'Consultant'
print(f'My name is {full_name} and i am {age} years old, i currently live at {address}, {city}. I studied {education} and i am a {job}')

# Exercise Level 2

# Question 1
# Check data types of variables
print(f'Data type of first_name: {type(first_name)}')
print(f'Data type of last_name: {type(last_name)}')
print(f'Data type of full_name: {type(full_name)}')
print(f'Data type of country: {type(country)}')
print(f'Data type of city: {type(city)}')
print(f'Data type of age: {type(age)}')
print(f'Data type of year: {type(year)}')
print(f'Data type of is_married: {type(is_married)}')
print(f'Data type of is_true: {type(is_true)}')
print(f'Data type of is_light_on: {type(is_light_on)}')

# Question 2
# Using the len() built-in function, find the length of your first name
length_first_name = len(first_name)
print(f'Length of first name: {length_first_name}')

# Question 3
# Compare the length of the first name and last name
length_last_name = len(last_name)
if length_first_name > length_last_name:
    print('First name is longer than last name')
elif length_first_name < length_last_name:
    print('Last name is longer than first name')
else:
    print('First name and last name have the same length')

# Question 4
# Declaring the variables
num_one = 5
num_two = 4

# Performing the operations
sum = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
div = num_one / num_two
mod = num_two % num_one
exp = num_one ** num_two
floor_div = num_one // num_two

# Display the results
print(f"Sum = {sum}")
print(f"Difference = {diff}")
print(f"Product = {product}")
print(f"Division = {div}")
print(f"Modulus = {mod}")
print(f"Exponentiation = {exp}")
print(f"Floor Division = {floor_div}")

# Question 5
import math

# Given radius
radius = 30

# Calculating the area of a circle using the given radius
area_of_circle = math.pi * radius ** 2
print(f"Area of circle with radius {radius}m is {area_of_circle:.5f} square meters")

# Calculating circumference of a circle with the given radius
circum_of_circle = 2 * math.pi * radius
print(f"Circumference of circle with radius {radius}m is {circum_of_circle:.5f}m")


# Taking user input for radius and calculating area
radius_input = float(input("Enter the radius of the circle: "))
area_of_circle_input = math.pi * radius_input ** 2

# Display the calculated area based on user input
print(f"Area of circle with radius {radius_input}m is {area_of_circle_input:.5f} square meters")

# Question 6
first_name = input('Enter your first name:')
last_name = input('Enter your last name:')
country = input('Which country are you from? ')
age = input('How old are you')

print(f'First name: {first_name}')
print(f'Last name: {last_name}')
print(f'Country: {country}')
print(f'Age: {age}')

# Question 7
import keyword

# Get all the keywords as a list
print(keyword.kwlist)