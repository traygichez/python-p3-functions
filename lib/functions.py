#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


greet_programmer()

def greet(name):
    print(f"Hello, {name}!")


greet("John")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


greet_with_default()  
greet_with_default("John")


def add(num1, num2):
    return num1 + num2

result = add(5, 3)
print(result) 


def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2


result = halve(8)
print(result)  

result = halve("string")
print(result)  

