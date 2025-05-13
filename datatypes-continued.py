"""
1. dicts -> objects
2. strings
3. list -> arrays
4. integers
5. floats
6. boolean
7. tuples
8. None
9. sets
"""

# 1.dicts -> collection of data stored in key - value (can be of any datatype) pairs
# we still use the curly braces {}
student = {
    "name": "Daud",
    "age": 20,
    "major": "Software Engineering",
    "scores": [34, 89, 76, { "model": "Audi" }],
    "location": "Eldoret"
}

# Accessing items in dicts -> with square brackets [] or the .get() method
print(student["age"])

print(student.get("location", "Nairobi"))

# Adding or updating dicts -> as long as the key exist, it is going to do an update
# else it is going to add
# modify age
student["age"] = 25

# add
student["class"] = {
    "name": "Web 9",
    "location": "Remote"
}

print(student)
print(student["class"]["name"])

print(student["scores"][2])

print(student["scores"][3].get("model"))

# delete items -> we use the del keyword or the .pop()
del student['location']

# the pop method gives you back the deleted value
deleted_value = student.pop("class")

print(deleted_value)

print(student)

# 2. sets -> unique elements -> we can create sets using curly brackets {} or the set()
# constructor
# A very good way to avoid duplication
random_values = {2, 3, 4, 3, 2, 4, 5}

print(random_values)

# empty curly braces still fall under dicts
empty_set = {}
# this is how we should create empty sets
correct_empty_set = set([2, 3, 4, 3])

print((correct_empty_set))

numbers = ['0712345678', '0712345679', '0712345678']

unique_numbers = set(numbers)

print(unique_numbers)

print(set('remove'))

# 3. list  -> ordered collection of items, similar to arrays in js
# we still use square brackets to create lists

students = [{"score": 40, "name": "John"}, {"score": 45, "name": "Jane"}]

# how te get length
print("Lenght of students list", len(students))

scores = [24, 67, 45]

scores[1] = 50
# this gives us an error
# scores[5] = 90
scores.insert(5, 90)
scores.insert(3, 60)

# the pop method without an argument removes the last value
# with argument, removes a value at the specified index
scores.pop(2)

print("Updated scores", scores)

# map method
def multiply_by_two(x):
    return x * 2

map_ierator = map(multiply_by_two, scores)
multiplied_scores = list(map_ierator)

print("Multiplied scores", list(map_ierator))

# filtering
def score_above_100(z):
    return z > 100
# lambda functions in python
# lambda x: x > 100
print("Filtered scores", list(filter(score_above_100, multiplied_scores)))

# 4. tuples -> similar to lists but they are immutable
# and we use the paranthesis ()

emails = ('john@gmail.com', 'jane@gmail.com')

print(emails[1])

temp_emails = list(emails)
temp_emails[1] = 'arif@gmail.com'
modified_emails = tuple(temp_emails)
print(modified_emails)


def two_highest(arr):
    # one liner
    return sorted(list(set(arr)), reverse=True)[:2]
    # get unique numbers only
    unique = list(set(arr))
    # sort from highest to lowest
    unique.sort(reverse=True)
    # we do slicing
    return unique[:2]

print(two_highest([4, 10, 10, 9]))