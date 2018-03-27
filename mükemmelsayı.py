print("""**********************
MUKEMMEL SAYI BULMA
*********************""")

sayi=int(input("Sayı: "))
bolenler=[]
bolentoplam=0
j=0
a=1

while a<sayi:
    if (sayi%a)==0:
        bolentoplam+=a
        print("bolenler: ",a)
        a+=1
    else:
        a+=1
        continue

if bolentoplam==sayi:
    print(sayi,"mükemmel bir sayıdır.")

else:
    print(sayi,"mükemmel bir sayı değildir.")