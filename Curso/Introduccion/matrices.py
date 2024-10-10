matrix = [
    [1, 2, 3, [4, 5, 6]],
    [4, 5, 6],
    [7, 8, 9],
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]

numbers_tuple = (1, 2, 3, 4, 5)
numbers_tuple_2 = 1, 2, 3, 4, 5

print(matrix)
print(matrix[0])
print(matrix[0][0])
print(matrix[0][3][0])
print(numbers_tuple)
print(numbers_tuple[0])

#numbers_tuple[0] = 10 # No se puede modificar un tuple

print(type(matrix)) # <class 'list'>
print(type(numbers_tuple)) # <class 'tuple'>
print(type(numbers_tuple_2)) # <class 'tuple'>
