#  Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique
d={}
n1=input("Enter your name:")
l1=input("Enter your language:")
d.update({n1:l1})
n2=input("Enter your name:")
l2=input("Enter your language:")
d.update({n2:l2})
n3=input("Enter your name:")
l3=input("Enter your language:")
d.update({n3:l3})
n4=input("Enter your name:")
l4=input("Enter your language:")
d.update({n4:l4})

print(d)
