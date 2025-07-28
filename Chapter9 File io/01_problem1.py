f=open("poem.txt")
content=f.read()
if("Twinkle" in content):
    print("the word Twinkle is present in the content")
else:
    print("the word Twinkle is not present in the content")

f.close()