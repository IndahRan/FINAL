'''
a = int(input("Masukkan panjang sisi 1 : "))
b = int(input("Masukkan panjang sisi 2 : "))

if a>0 and b>0 :
    if a==b :
        print("bangun datar persegi")
    else :
        print("bangun datar persegi panjang")
else:
    print("sisi pada bangun datar panjangnya harus >0")



a = int (input('Awal:'))
b = int (input('Akhir:'))
c = 0
if a> b:
    print('mohon maaf tanggal salah')
else:
    for i in range (a , b + 1):
        d = int (input ('Input data tanggal {}:' .format (i)))
        c = c + d

    print ('total pemasukan selama', (b + 1-a), ' hari adalah {} ', c)


m = int(input())
n = int(input())
for i in range(1, m+1):
    for j in range(1, n+1):
        if i%2 == 0 :
            print("0",end="")
        else :
            print("*",end="")
    print()
'''
