# def is_even(number):
#     return number % 2 == 0

# print(is_even(4))

# Assertion Errors
# assert gives you "AssertionError" if the value is false, if it's true it doesn't show anything
# assert 2 + 2 == 5 

# Syntax Errors, always when trying to debug starts from the bottom line
# print("Hello World"
      
# Exceptions (Runtime errors)

# Standard exception
## IndexError: Raised when a sequence subscript is out of range.
# my_list = [1, 2, 3]
# print(my_list[3])

## KeyError: Raised when a dictionary key is not found.
# my_dict = {
#     "name" : "Jess"
# }
# print(my_dict["age"])

## ValueError: Raised when a function receives an argument of the correct type but inappropriate value
int("abc")

## TypeError: Raised when an operation or function is applied to an object of inappropriate type. In the case bellow, len function is expected to be used with string, however you gave an INT type.
print(len(123))

# Attributes Errors: Raised when attributes reference or assignment fails

NoneType = None
NoneType.abc

# ZeroDivisionError: Raised when the second operand of a division or modulo operation is Zero.
print(10 / 0)

# FileNotFoundError: Raised trying to open a file that does not exist.
open('random_file.txt') 

# OS Errors: Raised for system-related errors, like "disk-full"

# User-defined Exceptions: Users create by subclassing the built-in Exception class
class myCustomError(Exception):
    pass
raise myCustomError("Hey Mate! There is an error.")

from module_1 import function_A

function_A.execute()

