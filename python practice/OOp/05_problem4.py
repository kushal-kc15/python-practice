# Design a class “Person”:
# The class should store personal details like name, age, and address.
# Implement methods to display the person's information, check if the person is an adult (18 years or older),
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display_info(self):
        print(f"name={self.name}")
        print(f"age of {self.name} is {self.age}")
        print(f"address of {self.name} is {self.address}")
        if(self.age<=22):
            print(f"marriage is illegal for  {self.name} ")
        elif(self.age>22):
            print(f"Marriage is legal for {self.name}")
Person1=Person("kushal",25,"Pokhara")
Person2=Person("Bibek",22,"parbat")
Person3=Person("Maira",23,"Dhangadi")
Person4=Person("kishmat",18,"Baglung")
Person1.display_info()
print()
Person2.display_info()
print()
Person3.display_info()
print()
Person4.display_info()
print()