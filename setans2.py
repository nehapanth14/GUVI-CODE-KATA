def get(num):
    if (num % 2) == 0:
       print("{0} is Even".format(num))
    elif num > 0 or num != 0:
       print("{0} is Odd".format(num))



try :
    num = int(input("Enter the number between 1 to 100000 : "))
except Exception:
    print ""
    print "       Invalid Input      "

if num <=100000:
    get(num)
else:
    print "Enter the number between 1 to 100000"

