#Fibonacci Serisini hesaplar

terims=int(input("Fibonacci terim sayısını giriniz."))
baslangic=int(input("Istediginiz baslangic degerini giriniz."))

if(baslangic==0):
    print("0 \n1")
    terims-=2
    baslangic=1

for i in range(terims):
    print(baslangic)
    baslangic+=baslangic
