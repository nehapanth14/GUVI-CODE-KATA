go = raw_input("Input a letter of the alphabet: ")

f = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
f = f.split(',')

if go in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % go)
elif go in f  :
        print("%s is a consonant." % go) 
else:
    print("  Invalid input , please enter a character  ")
