"""
    Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
    Once 'done' is entered, print out the largest and smallest of the numbers.
    
    If the user enters anything other than a valid number catch it with a try/except and put out an 
    appropriate message and ignore the number.
    
    Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
"""

value=[]
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        int(num)
    except:
        print("Invalid input")
    
    if num.isnumeric():
        value.append(int(num))

if len(value) != 0:
    print("Maximum is", max(value))
    print("Minimum is", min(value))
else:
    print("You have not entered any number")