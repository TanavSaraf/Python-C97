count=input("Enter a sentence:")
noOfCharacters=0
wordCount=1
for i in count :
    if(i==" ") :
        wordCount+=1

    noOfCharacters+=1

print(noOfCharacters,"'",count,"'")
print("")
print("word Count",wordCount)
#json = dictionary