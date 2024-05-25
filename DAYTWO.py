#Q no. 1 sum of positive numbers in integers
#Sol
"""
def sum_of_positive_number(numbers):
    positive_sum = 0

    for num in numbers:
        if num > 0:
            positive_sum += num
            
            
    return positive_sum


numbers_list=[9,-5,4,-6,-9,-4] 
result = sum_of_positive_number(numbers_list)
print("The sum of positive integers : ", result)
"""
#Q no. 2 create a programe that takes input and count words.
#Sol
"""#def count_words(input_text):
    #words = input_text.split()

    word_count = len(words)

    return word_count

user_input = input("Please enter Text or phrase: " )
result = count_words(user_input)
print("Total number of words: ", result)
"""
#Q implement a programe swaps value of two variables
#SOLv
"""
#def swap_with_temp_variable(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = input (" Please enter x variable : ")
y = input (" Please enter y variable : ")

x, y = swap_with_temp_variable(x, y)

print("After swaping : x=",x ,"y = ", y)
"""

