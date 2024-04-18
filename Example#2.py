#-------------------------------------------------------------------------
# Name:		    Lesson 5.1 Intro to Functions & Parameters
# Purpose:		Example #2
# Author:		  LastName. FirstInitial
# Created:		dd/mm/yyyy
#-------------------------------------------------------------------------
num = int(input("Enter a number: "))

# Example #1:
## Part (a) Create a function that will check if a number is even or odd
def even_odd(num: int):
    if num == 0:
        print("zero")
    elif (num % 2) == 0:
        print("even")
    else:
        print("your number is odd")

## Part (b) Use your function by calling it
even_odd(num)
