go = raw_input("Enter the input : ")

f = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
g = f.title()
f = f.split(',')
g = g.split(',')

if (go in f or go in g) :
    print "The entered value is an Alphabet "
else:
    print "Not an alphabet"
