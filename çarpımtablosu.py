print("""*********
ÇARPIM TABLOSU
*********""")

birler=list(range(10))

for i in range(1,10):
    for j in range(1,11):
        birler[j-1]=i*j
    print(birler)