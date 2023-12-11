key=3
y=float(input("Lütfen bir teklif giriniz: "))
while key>0:
    x=float(input("Lütfen bir teklif giriniz: "))
    if x>y:
        y=x
    key=key-1
print("Kazanan teklif: ",y)