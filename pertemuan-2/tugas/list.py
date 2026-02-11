#mendeklarasikan dan mem-print list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#list dapat memiliki dua value berbeda dengan isi  yang sama
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#mengetahui panjang list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#mengakses list dimulai dari 4 paling belakang hingga 2 dari belakang
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  #menampikan output seperti diatas jika terdapat apple dalam list
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
#mengganti value pada indeks ke 1 dengan yang baru
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 
#menambahkan watermelon pada indeks ke-2
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#menambahkan orange di indeks terakhir
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#menambahkan list tropical ke dalam list thislist
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#menghapus value list 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#menghapus value list menggunakan indeks
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#menghapus seluruh isi list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#melakukan perulangan sebanyak isi list

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#melakukan perulangan menggunakan panjang list

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#melakukan perulangan menggunakan while

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#shorthand for

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#memindahkan isi list ke list baru

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
newlist = [x for x in range(10) if x < 5]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]
#ketika x nya banana, diubah menjadi orange

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#mengurutkan berdasarkan kode ASCII

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#mengurtkan dengan kode ASCII dari bawah

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(key = str.lower)
print(thislist)
#gunakan ini ketika value terdiri dari upperdan lower

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#copy list ke list lain

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#MENGGABBUNGKAN 2 LIST
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
Append() Menambahkan elemen di akhir daftar
clear() Menghapus semua elemen dari daftar
copy() Mengembalikan salinan dari daftar
count() Mengembalikan jumlah elemen dengan nilai tertentu
extend() Menambahkan elemen dari daftar lain (atau iterable apapun) ke akhir daftar saat ini
index() Mengembalikan indeks dari elemen pertama dengan nilai tertentu
insert() Menambahkan elemen di posisi tertentu
pop() Menghapus elemen di posisi tertentu
remove() Menghapus item dengan nilai tertentu
reverse() Membalik urutan daftar
sort() Mengurutkan daftar
"""

