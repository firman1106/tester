# kelas kucing sebagai "definisi"
class mahasiswa:
  nama = None
  NIM = None
  jurusan = None

# membangun instance/variabel sebagai "objek nyata"
mahasiswa1 = mahasiswa()
mahasiswa1.nama = "Firman"
mahasiswa1.NIM = "1171030074"
mahasiswa1.jurusan = "Filsafat"

mahasiswa2 = mahasiswa()
mahasiswa2.nama = "Resa"
mahasiswa2.NIM = "1174030067"
mahasiswa2.jurusan = "Ekonomi"

mahasiswa3 = mahasiswa()
mahasiswa3.nama = "Indra"
mahasiswa3.NIM = "1174050011"
mahasiswa3.jurusan = "Hukum"
#Kita bisa menampilkan masing-masing atribut dari tiap instance:

print(mahasiswa1.NIM, mahasiswa1.nama, mahasiswa1.jurusan)
print(mahasiswa2.NIM, mahasiswa2.nama, mahasiswa2.jurusan)
print(mahasiswa3.NIM, mahasiswa3.nama, mahasiswa3.jurusan)