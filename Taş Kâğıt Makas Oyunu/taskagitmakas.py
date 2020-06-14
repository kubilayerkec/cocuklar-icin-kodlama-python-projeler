# Kubilay Erkeç
# kubilay@kubilay.net
# Udemy Eğitimleri: https://www.udemy.com/user/kubilay-erkec/

import random

def main():
    degerler = ["taş","kağıt","makas"]
    uretilenSayi = random.randint(0, 2)
    tahmin = int(input("Lütfen Tahmininizi Giriniz\n0: Taş 1: Kağıt 2: Makas\n"))

    print("Bilgisayarın seçtiği: ", degerler[uretilenSayi])

    if uretilenSayi == tahmin:
        print("Oyun Berabere")
    elif uretilenSayi == 0 and tahmin == 1:
        print("Kullanıcı kazandı")
    elif uretilenSayi == 0 and tahmin == 2:
        print("Bilgisayar kazandı")
    elif uretilenSayi == 1 and tahmin == 0:
        print("Bilgisayar kazandı")
    elif uretilenSayi == 1 and tahmin == 2:
        print("Kullanıcı kazandı")
    elif uretilenSayi == 2 and tahmin == 0:
        print("Kullanıcı kazandı")
    elif uretilenSayi == 2 and tahmin == 1:
        print("Bilgisayar kazandı")

if __name__ == '__main__':
    main()