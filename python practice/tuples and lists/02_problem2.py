# Write a program to accept marks of 6 students and display them in a sorted
# manner.
l=[]
m1=int(input("Enter marks of first student:"))
m2=int(input("Enter marks of second student:"))
m3=int(input("Enter marks of third student:"))
m4=int(input("Enter marks of fourth student:"))
m5=int(input("Enter marks of fifth student:"))
m6=int(input("Enter marks of sixth student:"))
l.append(m1)
l.append(m2)
l.append(m3)
l.append(m4)
l.append(m5)
l.append(m6)
l.sort()
print(l)