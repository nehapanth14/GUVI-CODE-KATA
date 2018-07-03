try:
    num = int(raw_input("Enter the number : "))
except Exception:
    print ""
    print "Invalid entry , Enter a number"

num = str(num) 
w = list(num)

p = len(w)

print"Number of digits is {0}".format(p)
