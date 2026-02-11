thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#SETS TIDAK BIDA MEMILIKI 2 VALUE YANG SAMA.TRUE DAN 1 DIANGGAP SAMA. FALSE DAN 0 DIANGGAP SAMA.

print(len(thisset))
myset = {"apple", "banana", "cherry"}
print(type(myset))
#MENGETAHUI PANJANG DAN TIPE

thisset = {"apple", "banana", "cherry"}


#PENGULANGAN PADA SET DAN PENGESEKKAN VALUE
for x in thisset:
  print(x)
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#PENAMBAHAN PADA SET
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#TIDAK HARUUS SET

#MENGHAPUS VALUE
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#PENGULANGAN PADA SET
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#PENGGABUNGAN SET
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

#HANYA MENAMPILKAN VALUE YANG ADA DI KEDUA SET
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

set1.intersection_update(set2)
print(set1)
#MERUBAH ISI SET1 DENGAN VALUE YANG ADA DI KEDUA SET

#ISI SET 1 YANG TIDAK ADA DI SET2
set3 = set1.difference(set2)
print(set3)
set3 = set1 - set2
print(set3)

set1.difference_update(set2)
print(set1)
#PERUBAHANDISIMPAN DI SET 1

#MENGISI SET 3 DENGAN VALUE YANG TIDAK DOUBLE
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
set1.symmetric_difference_update(set2)
print(set1)

#FROZEN SET
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

"""
copy() Mengembalikan salinan dangkal
difference() - Mengembalikan frozenset baru dengan selisihnya
intersection() & Mengembalikan frozenset baru dengan irisannya
isdisjoint() Mengembalikan apakah dua frozenset memiliki irisan
issubset() <= / < Mengembalikan True jika frozenset ini merupakan subset (sejati) dari frozenset lain
issuperset() >= / > Mengembalikan True jika frozenset ini merupakan superset (sejati) dari frozenset lain
symmetric_difference() ^ Mengembalikan frozenset baru dengan selisih simetrisnya
union() | Mengembalikan frozenset baru yang berisi gabungannya

add() Menambahkan elemen ke himpunan
clear() Menghapus semua elemen dari himpunan
copy() Mengembalikan salinan himpunan
difference() - Mengembalikan himpunan yang berisi perbedaan antara dua himpunan atau lebih
difference_update() -= Menghapus item dalam himpunan ini yang juga termasuk dalam himpunan lain yang ditentukan
discard() Menghapus item yang ditentukan
intersection() & Mengembalikan himpunan yang merupakan irisan dari dua himpunan lain
intersection_update() &= Menghapus item dalam himpunan ini yang tidak ada dalam himpunan lain yang ditentukan
isdisjoint() Mengembalikan apakah dua himpunan memiliki irisan atau tidak
issubset() <= Mengembalikan True jika semua item dari himpunan ini ada dalam himpunan lain
< Mengembalikan True jika semua item dari himpunan ini ada dalam himpunan lain yang lebih besar
issuperset() >= Mengembalikan True jika semua item dari himpunan lain ada dalam himpunan ini
> Mengembalikan True jika semua item dari himpunan lain yang lebih kecil ada dalam himpunan ini
pop() Menghapus elemen dari himpunan
remove() Menghapus elemen yang ditentukan elemen
perbedaan_simetris() ^ Mengembalikan himpunan yang berisi perbedaan simetris dari dua himpunan
pembaruan_perbedaan_simetris() ^= Memasukkan perbedaan simetris dari himpunan ini dan himpunan lain
gabungan() | Mengembalikan himpunan yang berisi gabungan himpunan
pembaruan() |= Memperbarui himpunan dengan gabungan himpunan ini dan himpunan lainnya
"""







