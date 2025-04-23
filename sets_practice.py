fruits = {"apples", "strawberries", "pears", "apples"}
print(fruits)
fruits.add("limes")
print(fruits)

with open('numbers.txt') as numbers_file:
    numbers = [int(n) for n in numbers_file.read().splitlines()]

# print(numbers)
no_neighbors = [
    n
    for n in numbers
    if n-1 not in numbers
    and n+1 not in numbers
]
print(no_neighbors)
numbers_set = set(numbers)
no_neighbors = [
    n for n in numbers
    if n - 1 not in numbers_set
    and n + 1 not in numbers_set
]

a = {2, 1, 3, 4, 7, 11, 18}
b = {1, 2, 3, 5, 7, 11, 13, 17}
print(a | b) # union
print(a & b) # intersection
print(a - b) # find all the items that are in one set and not in other
print(b - a) 
print(a ^ b)
numbers = [1,2,3,4,5,3,2]
print(len(numbers) == len(set(numbers)))
