nama = str(input("Masukkan nama : "))
z = int(input("Masukkan nilai yang akan dihitung:" ))
xn = 0
for x in range(z):
    x = x + 1
    nilai = int(input("Masukkan nilai anda ke-%d: "%(x)))
    xn += nilai
    ratarata = xn/z
print(nama+',','jumlah total nilai anda adalah: {}'.format(xn))
print("Hi,", nama+"!", "Hasil rata-rata anda adalah:", ratarata)