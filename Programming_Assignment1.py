## 1.Write a Python program to print &quot;Hello Python&quot;?

print("Hello Python")

## 2.Write a Python program to do arithmetical operations addition and division.?

def add(a,b):
    return a+b
def div(a,b):
    return a/b
print(add(5,6))
print(div(5,6))

## 3.Write a Python program to find the area of a triangle?

def area_of_triangle(b,h):
    return ((b*h)/2)
print(area_of_triangle(6,8))

## 4.Write a Python program to swap two variables?

def swap(a,b):
    print("Entered numbers are %s and %s ",a,b)

    temp = a
    a = b
    b = temp

    print("After swapping numbers are %s and %s",a,b)
swap(1,5)

## 5.Write a Python program to generate a random number?

import random
print(random.randint(1,10))