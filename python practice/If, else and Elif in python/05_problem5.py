# Write a program which finds out whether a given name is present in a list or not.
l=["kushal","bibek","kishmat","krishna"]
n=input("enter a name:")

if(n in l):
    print(f"{n} is present in list")
else:
    print(f"{n} isn't present in the list.")