"""
numbers = [3, 6, 2 ,8, 4]
print(max(numbers))
"""
"""
numbers = [3, 6, 2 ,8, 4, 10]
maxi = numbers[0]
for num in numbers:
    if num > maxi:
        maxi = num
print(maxi)
"""
"""
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
new_numbers = list(set(numbers))
print(new_numbers)
"""

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniq = []
for num in numbers:
    if num not in uniq:
        uniq.append(num)
print(uniq)
