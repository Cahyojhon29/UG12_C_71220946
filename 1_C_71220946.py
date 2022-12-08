kalimat = input("masukkan kata atau angka: ")
def reserve(kalimat):
    str= ""
    for i in kalimat:
        str = i + str
    return str
print(reserve(kalimat))

