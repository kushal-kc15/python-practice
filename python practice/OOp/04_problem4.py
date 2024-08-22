# Write a class “Circle”:
# The class should store the radius of a circle.
# Implement methods to calculate the area, circumference, and diameter of the circle.
class circle:
    def area(self,r):
        return 3.14159*r**2
    def circumference(self,r):
        return 2*3.14159*r
    def diameter(self,r):
        return 2*r
circ=circle()
r=int(input("Enter the radius:"))
print(f"The area of circle with radius {r} is {circ.area(r)}")
print(f"The circumference of circle with radius {r} is {circ.circumference(r)}")
print(f"The area of diameter with radius {r} is {circ.diameter(r)}")