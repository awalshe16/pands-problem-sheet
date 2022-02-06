#I am writing an application at the moment, in it I take an input of an amount
#in the form -9.44 (9 dollars and 44 cent), the issue there may or may not be a
#minus sign, and the bank takes in the amount in cent, (944). 
# Write a program called convert.py that takes in a float amount of dollars, and returns that
#absolute amount in cent.
#Surprised myself with this. initially absoluteamount result was 950.0000001, but I added int to make it a whole number and it worked!
numbertoconvert = float(input("enter input amount:"))
absoluteamount = abs(int(numbertoconvert * 100))
print ( '{} converted is {}'.format(numbertoconvert,absoluteamount))
