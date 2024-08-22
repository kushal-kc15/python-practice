# Write a program to find out the line number where python is present from ques 6.
lineno=1
with open("05_log.txt","r") as f:
    lines=f.readline()
for line in lines:
    if("python" in line):
        print(lineno)
        break
    lineno=lineno+1
else:
    print("sorry")