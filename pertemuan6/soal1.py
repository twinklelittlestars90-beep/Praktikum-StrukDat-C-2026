plat=['B 1234 ABC', 'D 8888 XYZ', 'A 111 TUV', 'B 2022 EFG']
ganjil=[]
genap=[]
def ganjilGenap (plat):
    for x in plat:
        platAngka=int(x.split()[1])
        if platAngka%2==0:
            genap.append(x)
        else:
            ganjil.append(x)
ganjilGenap(plat)
print(ganjil, genap)




