#Why does this expression cause an error? How can you fix it?
message = 'I have eaten ' + 100 + 'eggs'
print (message)
#causes error "can only concatenate str (not "int") to str". 
#the value you are concatenating needs to be same type, both int or str...
#To solve the issue, just add str to your number or value like: (https://stackoverflow.com/questions/51252580/how-to-resolve-typeerror-can-only-concatenate-str-not-int-to-str)
#message = 'I have eaten ' + str(99) + ' burritos.'
#print (message)
#7. Why is eggs a valid variable name while 100 is invalid? 
#becayse eggs is a string and 100 is an integer 
#8. What three functions can be used to get the integer, floating-point number, or string version of a value?
# integer = int(), floating-point number = float(), string = str()
