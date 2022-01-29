#Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py
#The inputs are the person's height in centimetres and weight in kilograms.
#The output  their BMI (You may need to look up how this is calculated)

#BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared (https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator)


## My own approach before research

#set height
#meter = 100
#height = int("enter height")/meter
#meter2 = height * height 

#set weight
#weight = int('enter weight in kilograms')

#BMI
#BMI = weight/meter2 

##After looking on google (https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g)

#Googled to understand meaning of a float (https://www.geeksforgeeks.org/float-in-python/#:~:text=Python%20float()%20function%20is,a%20number%20or%20a%20string.)
#Python float() function is used to return a floating-point number from a number or a string. 

from audioop import add


height = float(input("Enter you height in cm: "))
weight = float(input("Enter your weight in kg: "))
#BMI is weight / (height in cm/100) * (height in cm/100)
BMI = weight / (height/100)**2
#print('Your BMI is {BMI}') - almost

#Help page says print(f"You BMI is {BMI}")
#However, I do not understand meaning of f"You
#https://realpython.com/python-f-strings/
#f"you method is newest/most effective formatting method. I will stick to way in lecture for now

print ('Your BMI is {BMI}'.format(BMI =BMI))