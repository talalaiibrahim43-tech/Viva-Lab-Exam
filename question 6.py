
words = ["sun", "apple", "moon", "book", "green"]

result = [len(word) for word in words if word.endswith('n')]

print("Original Words:", words)
print("Lengths of Words Ending with 'n':", result)
