#upper (huruf jadi besar semua)
nama_lengkap = 'Firman Maulana Akbar'
print(nama_lengkap.upper())
#lower (huruf jadi besar semua)
nama_lengkap = 'Firman Maulana Akbar'
print(nama_lengkap.lower())

# pengecekan dengan menggunakan isX method
# apakah di nama lengkap adalah lower?
print(nama_lengkap.islower()) #ini hasilnya bolean
print(nama_lengkap.isupper())

# isalpha , apakah semuanya huruf, tanpa space, simbol, dan tanda baca
# isalnum , apakah semuanya huruf dan angka
# isdecimal, apakah str nya bentuk kosong, space, tab, new line
# is title, apakah semua katanya berawalan huruf besar

print("apakah nama lengkap adalah title? " + str(nama_lengkap.istitle()))

#cek komponen startswith endswith
print(nama_lengkap.startswith("Firm"))
print(nama_lengkap.endswith("bar"))

#gabung
pisah = ('firman','maulana','akbar') #ini adalah bentuk list yaa
print("-".join(pisah)) #menggabung yang ada dilist dengan tanda -

#sekarang dipisahin:
pisah = "Firman-Maulana-Akbar"
print(pisah.split('-')) #memisahkan dari setiap -

#alokasi karakter ljust, rjust, center
print("-"+"justify".ljust(11)+"-") #akan rata kiri dengan total stringnya adl 11
print("-"+"justify".rjust(11)+"-") #akan rata kanan dengan total stringnya adl 11
print("-"+"justify".center(11)+"-") #akan rata tengah dengan total stringnya adl 11
#total kaarakter 11 diatas, terhitung dengan kata justify, sisanya akan pakai spasi

#kalo mau biar ga pake spasi, maka caranya:
print("-"+"justify".ljust(11,"0")+"-") #akan rata kiri dengan total stringnya adl 11
print("-"+"justify".rjust(11,"0")+"-") #akan rata kanan dengan total stringnya adl 11
print("-"+"justify".center(11,"0")+"-") #akan rata tengah dengan total stringnya adl 11

#menghilangkan char pakai strip
contoh="wkwk FIRMAN wkwk"
print(contoh.strip("wkwk"))
#kalo strip dikosongin, maka auto ngilangin spasi
contoh="wkwk FIRMAN wkwk"
print(contoh.strip()) #bntar agak confus


