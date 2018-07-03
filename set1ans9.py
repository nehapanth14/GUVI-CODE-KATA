
n = input("Enter the value of n : ")
K = input("Enter the value of K : ")


N = range(1,n+1)

N= N[0:K]
l = 0
for i in N:
    l += i

print l
