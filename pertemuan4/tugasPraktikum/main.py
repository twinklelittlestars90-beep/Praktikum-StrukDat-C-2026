from kurs import kurs
from tabulate import tabulate
from konverter import id_ke_asing, asing_ke_asing, asing_ke_id, sama
header = ['Kode', 'Kurs']
tampilkanKurs = [
   ['USD', kurs["USD"]],
   ['EUR', kurs["EUR"]],
   ['JPY', kurs["JPY"]],
   ['SGD', kurs["SGD"]]
]
print('=== KONVERTER MATA UANG ===')
print(tabulate(tampilkanKurs, headers=header, tablefmt="fancy_grid"))

dari=input("Dari (IDR/USD/EUR/SGD/JPY):")
ke=input("Ke (IDR/USD/EUR/SGD/JPY):")
dari=dari.upper()
ke=ke.upper()
jumlah= int(input("Jumlah:"))
if dari=="IDR":
   hasil=id_ke_asing(ke, jumlah)
elif dari!="IDR" and ke=="IDR":
   hasil=asing_ke_id(dari, jumlah)
elif dari==ke:
   hasil=sama(jumlah)
else:
   hasil=asing_ke_asing(dari, ke, jumlah)
print(f"{jumlah} {dari}= {hasil:.2f} {ke}")
