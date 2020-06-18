# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

def main():
    sayilar = []
    for k in range(5):
        sayi = int(input("Aritmetik Ortalaması Hesaplanacak Sayıyı Giriniz: "))
        sayilar.append(sayi)

    toplam = sum(sayilar)
    miktar = len(sayilar)
    sonuc = toplam / miktar
    print("işlem sonucu: ", sonuc)

if __name__ == '__main__':
    main()