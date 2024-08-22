f=open("01_poem.txt")
text=f.read()
if "twinkle" in text:
    print("the file contains the word twinklw")
else:
    print("The file doesnt contain the word Twinkle")
f.close()
