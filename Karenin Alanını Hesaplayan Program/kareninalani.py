kenar = int(input("Karenin bir kenarının ölçüsünü giriniz: "))
if kenar <= 0:
    print("Karenin kenarı sıfır veya sıfırdan küçük olamaz")
else:
    alanhesabi = kenar * kenar
    print("Karenin alanı", alanhesabi,sep=" = ")