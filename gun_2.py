balance=float(input("Lütfen hesap bakiyenizi giriniz: "))
withdraw=float(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
if balance<withdraw:
    print("Yetersiz bakiye")
else:
    last=balance-withdraw
    print("""İşleminiz tamamlandı. 
Lütfen kartınızı almayı unutmayınız.""",)
    print("Kalan bakiye: ",last)
input()