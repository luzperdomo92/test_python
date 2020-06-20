def fibon(n):
    a = b = 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return (result)

numbers = fibon(50)
print(numbers, end= '')
