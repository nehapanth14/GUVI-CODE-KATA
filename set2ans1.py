import math as m


try:
    n = int(raw_input("Enter a number : "))
    p = int(raw_input("Enter the power: "))
except Exception:
    print ""
    print " Invalid Entry , Enter a number "

ans = m.pow(n,p)

print ("The answer is {0}".format(ans))
