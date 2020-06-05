# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

print("İşlemler:","1 -> Toplama","2 -> Çıkarma", "3 -> Bölme", "4 -> Çarpma", sep="\n")
sayi1 = int(input("İşlem yapılacak ilk sayıyı giriniz: "))
sayi2 = int(input("İşlem yapılacak ikinci sayıyı giriniz: "))
islem = int(input("İşlemin ne olduğunu giriniz: "))

sonuc = 0
if islem == 1:
    sonuc = sayi1 + sayi2
elif islem == 2:
    sonuc = sayi1 - sayi2
elif islem == 3:
    sonuc = sayi1 / sayi2
elif islem == 4:
    sonuc = sayi1 * sayi2

print("işlem sonucu: ", sonuc)