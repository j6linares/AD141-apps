""" Exercise 3

Write a program that accepts a string from the user.

    Determine and print the following information about the string:

        Does it end in a period?

        Does it contain all alphabetic characters?

        Is there an 'x' in the string?

    Create and print a new string that has all occurrences of e changed to E. """

string=input("string: ")
print(string.endswith("."))
print(string.isalpha())
print(string.find("x"), 'x' in string)
print(string.replace("e", "E"))