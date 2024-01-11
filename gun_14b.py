sentence=input("Benzersiz harflerini göstermemiz için bir şeyler yazın: ")
letters=[]
for i in sentence:
    if i in letters:
        letters.remove(i)
    else:
        letters.append(i)
print("Tekrar etmeyen harfler->",letters)