
import math

numbers = [1, 4, 7, 9, 12, 16, 20, 25, 30]

result = [x for x in numbers if x >= 0 and math.isqrt(x) ** 2 == x]

print("Original Numbers:", numbers)
print("Perfect Square Numbers:", result)
