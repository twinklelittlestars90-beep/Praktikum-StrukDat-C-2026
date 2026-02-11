thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
}
print(thisdict)
print(thisdict["brand"])
# MENDEKLARASIKAN DICTIONARIES DAN MENGAKSES NYA. DUPLICATE VALUE AKAN MENIMPA VALUE SEBELUMNYA

#MENGETAHUI PANJANG DICTIONARIES
print(len(thisdict))
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

"""
print(type(thisdict))
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

x = thisdict.get("year")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) 

x = car.items()
print(x) #before the change
car["year"] = 2020
print(x)

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x)

#memeriksa apakah ada keys ini dalam dict
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#MENGUBAH ITEMS
thisdict.update({"year": 2020})
#mMENGHAPUS ITEM
thisdict.pop("year")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict.clear()
print(thisdict)

#PERULANGAN DICT
for x in thisdict:
  print(x)

for x in thisdict.keys():
  print(x)
  
#MENGGUNAKAN FOR UNTUK PRINT KEY

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)
#MENGGUNAKAN FOR UNTUK PRINT VALUES

for x, y in thisdict.items():
  print(x, y)
#MENGGUNAKAN FOR UNTUK PRINT KEYS DAN VALUES

#COPY DICT AWAL KE DICT BARU
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#MEMBUAT DICT DALAM DICT
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#MEMBUAT 3 DICT LALU MEMASUKKAN NYA DALAM SEBUAH DICT BARU
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
