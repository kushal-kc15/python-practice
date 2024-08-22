# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class programmer:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display_info(self):
        print(f"programmer's name: {self.name}")
        print(f"programmer's age: {self.age}")
        print(f"programmer's salary: {self.salary}")
        print("company:microsoft")
programmer1=programmer("kushal",20,"100000")
programmer2=programmer("bibek",21,"10000")
programmer3=programmer("kishmat",22,"1000")
programmer4=programmer("maira",23,"100")
programmer1.display_info()
print()
programmer2.display_info()
print()
programmer3.display_info()
print()
programmer4.display_info()
print()