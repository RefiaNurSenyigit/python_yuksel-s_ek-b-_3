words = ["cat", "car", "code", "home", "learn", "fun", "job",
          "love", "friend", "zoo", "enjoy", "happiness", "family", "goal", "desire"]
result=[]
word=input("Bir harf giriniz: ")
for i in words:
    if word in i[0]:
        result.append(i)
print(result)