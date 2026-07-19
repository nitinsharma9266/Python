f=open("poem.txt")
text=f.read()


if("ansh" in text ):
    print("the word Twinkle is present in the list .")

else:
    print("the word Twinkle is not present in the list .")
     

f.close()