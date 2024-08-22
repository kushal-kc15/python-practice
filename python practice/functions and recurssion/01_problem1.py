# Write a program using functions to find greatest of three numbers.
def greatest(a,b,c):
    if(a>b and a>c):
        print("a is the greatest number")
        return
    elif(b>a and b>c):
        print("b is the greatest number.")
        return
    else:
        print("c is the greatest number.")
        return 
greatest(66,44,235)