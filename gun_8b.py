a=int(input("""Boya göre kilo aralığını sorgulamak için 1'e,
Vücut kitle indeksini hesaplamak için 2'ye basınız.
--->"""))
if a==1:
    q=float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
    print("ideal kilonuz",round(18.5 * (q ** 2), 2), "-", round(24.9 * (q ** 2), 2),"aralığındadır.")
    input()
elif a==2:
    r=float(input("Lütfen kilonuzu giriniz: "))
    e=float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
    i=float(r/(e**2))
    if i<18.5:
         print("sağlıksız zayıf")
    elif 18.5<i<24.9:
         print("normal")
    elif i>24.9:
        print("sağlıksız kilolu")
input()