""" Exercise 4

Write a program that asks the user to enter a sentence.

    The program should determine and print the following information:

        The first character in the string of text and the number of times it occurs in the string.

        The last character in the string of text and the number of times it occurs in the string. """

sentence=input("enter a sentence: ")
print(sentence[0], sentence.count(sentence[0]))
print(sentence[len(sentence)-1], sentence.count(sentence[len(sentence)-1])) # sentence[-1] is the last character