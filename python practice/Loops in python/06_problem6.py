
# 6. Write a program to calculate the factorial of a given number using for loop.
num=int(input("Enter a number:"))
product=1
for i in range(1,num+1):
    product=product*i
print(f"the factorial of {num} is {product}.")
    