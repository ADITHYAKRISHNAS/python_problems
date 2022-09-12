# python program for hello world
#print("hello world")
# Add two number
#num1 = input('Enter the first number: ')
#num2 = input('Enter the second number: ')
#sum = float(num1) + float(num2)
#print('The sum of {0} and {1} is {2}'.format(num1,num2,sum))
# find the square root
#number = float(input("Enter the number"))
#Sqr_rt = number ** 0.5
#print("the square root of %f is %f"%(number,Sqr_rt))
print("Enter the sides of triangle")
num1 = float(input("Enter the first side: "))
num2 = float(input("Enter the second side: "))
num3 = float(input("Enter the third side: "))
s = (num1+num2+num3)/2
area = (s*(s-num1)*(s-num2)*(s-num3))
print("area of the triangle is %0.2f" %area)
