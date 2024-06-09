import sys

try:
 x = int(input("X: "))
 y = int(input("Y: "))
except ValueError:
 print("Invalid value")
 sys.exit(1)

try:
 result = x/y
except ZeroDivisionError:
 print("Value can not Divide by Zero")
 sys.exit(1)

print(f"{x} / {y} = {result}")