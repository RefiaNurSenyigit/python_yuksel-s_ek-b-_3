def is_leap(year):
    leap = False
    mod=year%4
    mod2=year%100
    mod3=year%400
    if mod==0 or mod3==0:
        if mod2==0 and mod3==0 or mod==0 and mod2!=0:
            leap=True
        elif mod2==0 and mod3!=0:
            leap=False
    return leap

year = int(input("Lütfen kontrol etmek istediğiniz yılı giriniz: "))
print(is_leap(year))