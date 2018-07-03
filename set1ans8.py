N = int(input("Enter a number :"))
s = 0

if N<0:
    print "Enter a positive number"

while N!=0:
    s += N
    N -= 1

print s
