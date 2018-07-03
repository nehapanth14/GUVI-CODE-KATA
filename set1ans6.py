def special(year): # THIS IS FOR YEAR ENDING WITH 00 EX: 1900
    c = str(year)
    d = list(c)
    if d[2:4]==['0','0'] and year%400==0:
        print ("{0} is a leap year".format(year))
    elif d[2:4]==['0','0'] and year%400 != 0:
        print ("{0} is not a leap year".format(year))
    else:
        print""
        
def normal(year): # THIS IS FOR GENERAL YEAR EXCLUDING THE CENTURY
    c = str(year)
    d = list(c)
    if d[2:4]!=['0','0'] and (year%4 == 0):
        print ("{0} is a leap year".format(year))
    elif d[2:4]!=['0','0'] and (year%4 != 0):
        print("{0} is not a leap year".format(year))
    else:
        print""


year = int(input("Enter a year: "))

special(year)
normal(year)


