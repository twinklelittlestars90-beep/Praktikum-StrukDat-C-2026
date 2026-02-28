stok_barang=[15, 40, 30, 10, 25]
stok_barang[3]=50
stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)
total=sum(stok_barang)
panjang=len(stok_barang)
nilai="Stok Aman" if total/panjang>20 else "Waspada"
print(nilai)

data_aktivitas={
   'p1':{"nama":"Diki","poin": 88}, 
   'p2':{"nama":"Aqul","poin": 45},
   'p3':{"nama":"Abid","poin": 92},
   'p4':{"nama":"Rehan","poin": 70}
   }
for x in data_aktivitas.values():
    if x["poin"]>80:
        print(f"{x["nama"]} mendapatkan predikat Gold")
    elif x["poin"]>=50 and x["poin"]<=80:
        print(f"{x["nama"]} mendapatkan predikat silver")
    elif x["poin"]<50:
        print(f"{x["nama"]} mendapatkan predikat bronze")

    

ukm_coding={"Andi", "Budi", "Caca", "Deni"}
ukm_robotik={"Caca", "Deni", "Euis", "Fafa"}

coding_saja=ukm_coding-ukm_robotik
print(coding_saja)
unik=ukm_coding|ukm_robotik
print(unik)
if "Andi" in ukm_robotik:
    print(True)
else:
    print(False)



gudang_pc = [
 {"item": "Monitor", "harga": 1500000, "stok": 5},
 {"item": "Keyboard", "harga": 400000, "stok": 12},
 {"item": "Mouse", "harga": 250000, "stok": 20}
]
gudang_pc[1].update({"kategori":"Aksesoris"})
print(gudang_pc)
gudang_pc.append({"item":"Headset", "harga":350000, "stok":8})
print(gudang_pc[-1])

for x in gudang_pc:
    total=x["harga"]*x["stok"]
    print(f"{x["item"]} | total aset: Rp{total}")