# Regular function
def add(a, b):
    return a + b

# Lambda function
add_lambda = lambda a, b: a + b

# Using the lambda function
result = add_lambda(5, 3)
print(result)  # Output: 8

points = [(1, 2), (3, 1), (5, -1)]
points.sort(key=lambda point: point[1])
print(points)  # Output: [(5, -1), (3, 1), (1, 2)]

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
