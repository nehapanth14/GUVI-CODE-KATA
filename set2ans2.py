def palindrom(inp):    
    c = list(str(inp))
    d = c[::-1]
    if c == d:
        print "Its a palindrom"
    else:
        print "Its not a palindrom"


inp = int(raw_input("Enter a number below 1000 : "))


if inp >1000:
    print "Enter a value below 1000"
else:
    palindrom(inp)


