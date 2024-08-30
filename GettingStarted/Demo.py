"""
Author: Rose McCormack
Version: 28 August 2024

Description: This will be the first demonstration file for
CIS 3680 - Programming Software Solutions. I hope to use this
file to demonstrate data types and basic print statements. 
"""

# Asking the user their name and age
name = input("Please enter your name? ")
age = int(input("How old are you? "))

# Returns statement for the user from their inputs
print("Your name is " + name + " and you are", age, "years old.")

# Second example
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

def add(num1, num2):
    return num1 + num2

print(add(first, second))


