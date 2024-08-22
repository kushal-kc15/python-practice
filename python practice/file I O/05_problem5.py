# Write a program to mine a log file and find out whether it contains ‘python’.

with open ("05_log.txt","r") as f:
    content=f.read()

if ("Python" in content):
    print("The file contain the word python.")
else:
    print("Word doesn't found.")