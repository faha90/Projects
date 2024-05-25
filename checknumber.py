"""""
Write a program that checks if a given number is        positive, negative, or zero.
Solution:
"""
def check_number (num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
num = int(input("Enter The Number: "))
result = check_number(num)
print(f"The number {num} is {result}.")
