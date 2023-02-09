from functions_for_output import *
import random

print("Enter the first value")
a = convertInput(input('input: '))
print("Enter the second value")
b = convertInput(input('input: '))
if(a==b):
    print("They're the same")
else:
    print("They're different")