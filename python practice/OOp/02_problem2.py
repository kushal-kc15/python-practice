# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
class Calculator:
    def square(self,number):
        return number**2
    def cube(self,number):
        return number**3
    def square_root(self,number):
        return number**0.5
calc=Calculator()
num=int(input("Enter a number:"))
print(f"square of {num} is:{calc.square(num)}")
print(f"cube of {num} is:{calc.cube(num)}")
print(f"square_root of {num} is:{calc.square_root(num)}")