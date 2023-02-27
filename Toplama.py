toplam = 0
while True:
    a = input("Lütfen sayı giriniz veya sonlandırmak için 'q' ya basınız : ")
    if a == "q":
        break
    else:
        a = int(a)
        toplam += a
print("Sonuç: ",toplam)

