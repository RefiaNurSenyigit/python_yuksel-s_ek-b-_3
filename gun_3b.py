gun=input("Lütfen randevu almak istediğiniz günü giriniz: ")
saat=int(input("Lütfen randevu almak istediğiniz saati giriniz: "))
if gun=="pazar"or gun=="cumartesi":
    print("Maalesef o gün kapalı...")
else:
    if 10<=saat<=21:
        print("Randevunuz oluşturuluyor...")
    else:
        print("Maalesef seçtiğiniz saatte randevu bulunamamakta...")
input()