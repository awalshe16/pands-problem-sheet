#Write a program that asks a user to input a string and outputs every second letter in reverse order.
#$ python secondstring.py
#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#.o zletrv pu o wr cu h
rawString = input("please enter a string:")
#Had to check out (https://www.w3schools.com/python/trypython.asp?filename=demo_howto_reverse_string)
ReverseString = rawString[::-2]
print(ReverseString)
#Took me some messing around with different numbers within [] to figure it out 
#Got some help from (https://codippa.com/how-to-print-characters-at-even-position-in-string-in-python/)
