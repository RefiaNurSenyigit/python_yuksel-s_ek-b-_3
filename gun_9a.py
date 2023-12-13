alpha= ["A","B","C","D","E","F","G","H",
        "I","J","K","L","M","N","O","P",
        "R","S","Ş","T","U","V","W","X",
        "Y","Z"
        ]
print("give me 3-number code take a 3-letter word")
a=int(input("first: "))
b=int(input("second: "))
c=int(input("third: "))
if 0<=a<=26 or 0<=b<=26 or 0<=c<=26:
    print(alpha[a]+alpha[b]+alpha[c])
else:
    print("Please enter between 0 to 26")
