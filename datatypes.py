# Datatypes

""" -> doc strings
Rules associated with variables
1. Naming convention is snake_case
2. Cannot use keywords
3. Variables must contain values when initialized
4. We use indentation to define code blocks
5. Have descriptive variable names
6. functions must be defined with the def
7. We do not need semicolons in python
"""

# 1. strings
message = "Intro to python"
greeting = int("8")



print(type(greeting))

# interpolation in python using F-strings
first_name = "John"
full_name = f"{first_name} Doe"

print(first_name + full_name)

print(full_name)

# 2 & 3 integers and floats
# when combining integers and floats in mathematical
# expressions, integers are always converted to floats
print(-3 + 7)
print(-3.0 * 7)

# integers are whole numbers and they have the type int
print(type(3 * (2 - 4) + 4))

# floats -> any numbers with decimal points
total = -0.7 + -2.5
print(total)
print(type(total))
print(type(7 / 3))

print(int(2.5 + 1.4))
print(round(2.5 + 1.4))

cost = 12.5


# 4. booleans -> True/False
is_adult = True

# boolean expressions -> a logical statement that can either be True/False
# Logical operators -> and/or/not
# Comparison operators -> ==
# Numbers operators -> >
print(bool(""))
print(bool(0))

print(4 > 9)


# 5. dictionaries, sets -> are objects in js
person = {
    # the keys must be in strings
    "name": "John",
    "age": 4,
    "address": {
        "county": "Mombasa"
    }
}

# square bracket notation
print(person['name'])
print(person['address']['county'])

# .get method
print(person.get("age"))
print(person.get('address')['county'])

# destructuring
age, county = person['age'], person['address']['county']
print(person['age'], person['address']['county'])


# 6. list 7. tuples -> arrays,
#
colors = ['red', 'green', 'blue']

print(colors[0])

# we use paranthesis
# tuples are immutable

scores = (1, 2, 3, 4)
print(scores[3])
# oop

# None -> null & undefined


day = None

day = "Tuesday"