from kurs import kurs
def id_ke_asing(ke, jumlah):
    return jumlah/kurs[ke]
def asing_ke_id(dari, jumlah):
    return jumlah*kurs[dari]
def asing_ke_asing(dari, ke, jumlah):
    return jumlah*kurs[dari]/kurs[ke]
def sama(jumlah):
    return jumlah