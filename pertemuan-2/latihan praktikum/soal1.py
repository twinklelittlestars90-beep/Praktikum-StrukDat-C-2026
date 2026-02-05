stok=[15, 50, 30, 25,40]
stok.append(100)
stok.insert(2, 75)
stok.sort(reverse = True)
jumlah=0
for x in stok:
  jumlah=jumlah+x
panjang=len(stok)
rata=jumlah / panjang
print(rata)
print(stok)