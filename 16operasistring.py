
#menyambung string (concantenate)
nama_depan = "Firman "
nama_tengah = "Maulana "
nama_belakang = "Akbar"
nama_lengkap = nama_depan + nama_tengah + nama_belakang
print (nama_lengkap)

#menghitung panjang string (len)
print(len(nama_lengkap))

#mengecek apakah ada char string di string
cari = "F"
cek = cari in nama_lengkap
print("char "+cari+ " ada di kata "+nama_lengkap+ " : " +str(cek))

# mengulang string
print('wk'*10)
print(5*"haha")

#indexing (mengambil karakter ke-0 dari sebuah string)
print(nama_lengkap[0])
#mengambil karakter ke-1 dari string
print(nama_lengkap[1])
#jadi, untuk indexing ini, huruf pertama dihitung sebagai huruf ke-0, dst
print(nama_lengkap[-1]) #ini dari belakang, huruf pertama dari belakang adl -1
print(nama_lengkap[0:4]) # mengambil string dari karakter ke 0 sampai ke-4
#huruf ke 4 harusnya "a" kebawa, tapi anehnya di python mah yg terakhir ga kebawa
#mengambil huruf tapi diloncat, misal:
print(nama_lengkap[0:8:2]) #artinya mengambil huruf ke 0-8 tapi di loncat 2 2

#item terkecil atau terbesar nilai ascii code nya
print(min(nama_lengkap)) #nilai ascii code terkecil adalah "spasi"
print(max(nama_lengkap)) #nila ascii code terbesar adalah "u"

#mengetahui berapa sih nilai ascii code itu? gini caranya:
print(ord(" ")) #nilai ascii code "spasi" adalah 32
print(ord("F")) #nilai ascii code "F" adalah 70
print(chr(70)) #nilai 70 adalah ascii code untuk huruf "F"

#menghitung jumlah chr dalam string
print(nama_lengkap.count("a")) # ada berapa jml huruf "a" dalam string "Firman Maulana Akbar" adalah 5
