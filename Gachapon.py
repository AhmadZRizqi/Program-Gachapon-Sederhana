b = int(input("Masukkan berapa kali jumlah pengacakan yang anda inginkan:"))
c = 0
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []

while c < b:
    c += 1

    import random
    a = random.randint (1,100)

    if a <= 100 and a > 60:
        print (c,".Bintang 1. Ampas, Coba Lagi")
        c1.append("1")
    elif a <= 60 and a > 30:
        print (c,".Bintang 2. Hampir Ampas")
        c2.append("1")
    elif a <= 30 and a >13:
        print (c,".Bintang 3. Lumayan")
        c3.append("1")
    elif a <= 13 and a > 1:
        print (c,".Bintang 4. Hampir dapet Jackpot")
        c4.append("1")
    elif a == 1:
        print (c,".Bintang 5. JACKPOT!!!")
        c5.append("1")

d1 = len(c1)
d2 = len(c2)
d3 = len(c3)
d4 = len(c4)
d5 = len(c5)

print("\nJumlah Bintang 1 yang didapat: ",d1)
print("Jumlah Bintang 2 yang didapat: ",d2)
print("Jumlah Bintang 3 yang didapat: ",d3)
print("Jumlah Bintang 4 yang didapat: ",d4)
print("Jumlah Bintang 5 yang didapat: ",d5)

input("\nPress Enter to Exit")
