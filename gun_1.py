anahtar=0
while anahtar==0:
    sayi=int(input("Lütfen bir sayı giriniz: "))
    if 1<=sayi<=100:
        odd_even=sayi%2
        if odd_even==0 and 2<=sayi<=5 or odd_even==0 and 20<sayi:
            print("Not Weird")
        elif odd_even==1 or odd_even==0 and 6<=sayi<=20:
            print("Weird")
        anahtar=1
    else:
       print("Lütfen 1 ile 100 arasında bir sayı giriniz!")
input()
