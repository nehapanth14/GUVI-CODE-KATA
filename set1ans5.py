print "Enter three numbers"


try :
    num1 = int(input("Enter the number 1 : "))
    num2 = int(input("Enter the number 2 : "))
    num3 = int(input("Enter the number 3 : "))
except Exception:
    print ""
    print "       Invalid Input      "

    

if (num1 > num2 and num1 > num3):
    print ("{0} is the greatest number ".format(num1))
elif num2 > num3:
    print ("{0} is the greatest number ".format(num2))
else:
    print ("{0} is the greatest number ".format(num3))
