print "Enter three numbers"

num1 = input("Enter the number 1 : ")
num2 = input("Enter the number 2 : ")
num3 = input("Enter the number 3 : ")

if (num1 > num2 and num1 > num3):
    print ("{0} is the greatest number ".format(num1))
elif num2 > num3:
    print ("{0} is the greatest number ".format(num2))
else:
    print ("{0} is the greatest number ".format(num3))
