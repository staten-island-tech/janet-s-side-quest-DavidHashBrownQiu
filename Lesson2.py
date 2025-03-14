"""fruits = ["apples", "banana", "orange"]

for i in range(len(fruits)):
    print(i+1, fruits[i])

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

word = "University"

for index, letter in enumerate(word, start=1):
    print(index, letter)

colors = ("red", "green", "blue")

for index, color in enumerate(colors, start=1):
    print(index, color)"""

"""days = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday"}

for index, key in enumerate(days, start=1):
    print(index, key, days[key])"""

"""students = ["Alice", "Bob", "Charlie"]
indexed_students = [(i, student) for i, student in enumerate(students, start=1)]
print(indexed_students)"""

"""universities = {"dog", "cat", "goat"}

for i in enumerate(universities, start=1):
    print(i)"""

#-------------------------------------------------------------------------------
"""
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)"""

numbers = [1, 2, 3, 4, 5]

# Use map() to double the numbers
doubled_numbers = map(lambda x: x * 2, numbers)
#lamda is an anonymous function that works in this case
#putting numbers at the end tells map() to loop through that list

print(list(doubled_numbers))
#make it into a list

data = [
    ["Store Name", "Day 1", "Day 2", "Day 3"],  # Header row (skip this)
    ["Store A", 5000, 7000, 6500],
    ["Store B", 8000, 6000, 7500]
]

for row in data[1:]:  # Skip the first row
    print(row)
#detects how many rows and removes one of them in chronological order

def calcRow(data):
    row_totals = {}

    for row in data[1:]:  # Skipping the first row
        sales = map(int, row[1:])  # Convert sales to numbers

    return row_totals

# Example Data

totals = calcRow(sales_data)
print(totals)