
numbers = [2, 4, 6, 8, 10, 12]

even_numbers = [x for x in numbers if x % 2 == 0]

squares = [x ** 2 for x in even_numbers]

result = [x for x in squares if x > 100]

print("Even Numbers:", even_numbers)
print("Squares:", squares)
print("Squares Greater Than 100:", result)
