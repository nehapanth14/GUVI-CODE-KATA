

def c(num):
    if num > 0:
       print("Positive number")
    elif num == 0:
       print("Zero")
    else:
       print("Negative number")

num = float(input("Enter the number between 1 to 1000 : ")) # Getting the input from user


if num >1000:      #Checking whether the user has entered the number within 1000
    print "please enter the number within 1000"
else:
    c(num) 
     

  
