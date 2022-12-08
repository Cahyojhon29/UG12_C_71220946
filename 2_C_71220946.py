angka = input ("masukkan angka :" )
hitung = input ("masukkan angka yang dihitung : ")

sum = 0
for each in angka:
    if each == hitung:
        sum = sum + 1

print ("angka",hitung,"muncul sebanyak",sum,"kali")
