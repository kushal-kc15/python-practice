# Write a program to print multiplication table of a given number using for loop.
a=int(input("Enter a number for multiplication:"))

for i in range(1,11):
    mul=a*i
    print (f"{a}X{i}={mul}")
    i=i+1