"""
numbers = [5,2,5,2,2]
for num in  numbers:
    print("x" * num)
"""

numbers = [5,2,5,2,2]
for count in numbers:
    output = ""
    for count1 in range(count):
        output += "x"
    print(output)
