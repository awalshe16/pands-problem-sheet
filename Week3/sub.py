#Program to subtract one number from another. 
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations

x = int(input('Enter first number:'))
y = int(input('Enter second number:'))
answer = x-y

print("{} minus {} is {}".format(x,y,answer))

#Note2self : input means that you should be entering something into the terminal to expect a result
#the order in the brackets at the end (x,y,answer) is important