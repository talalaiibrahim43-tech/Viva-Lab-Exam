
words = ["cat", "apple", "dog", "banana", "book"]

result = [word.upper() for word in words if len(word) > 3]

print("Original List:", words)
print("Uppercase Words:", result)
