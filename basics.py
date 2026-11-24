from calculator import add, subtract, multiply, divide
import sys
print(sys.version)
print(sys.version_info)
print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", round(divide(5, 3), 2))