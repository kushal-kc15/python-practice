# . A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
word = "bad"
with open ("4_file.txt","r") as f:
    content=f.read()
# contentnew=content.replace(word,"#####")

if (word in content):
    contentnew=content.replace(word,"####")
    with open("file.txt","w") as f:
        f.write(contentnew)
    print("Word found successfully")
else:
    print("Word not found")

# with open("file.txt","w") as f:
#     f.write(contentnew)