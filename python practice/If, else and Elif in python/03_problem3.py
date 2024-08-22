# . A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams
a="hello, this is kushal kc. click this link to make a lot of money"
if("make a lot of moneey" in a):
    print("This is a spam comment")
elif("buy now" in a):
    print("This is a spam comment")
# elif("click this" in a):
#     print("This is a spam comment")
elif("subscribe" in a):
    print("This is a spam comment")
else:
    print("This is not a spam comment.")

