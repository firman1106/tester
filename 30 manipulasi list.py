# manipulasi list
# index (data ke-)
data = ["firman","maulana","akbar"]
# firman index ke 0 atau ke -3 (dari belakang)
# maulana index ke 1 atau ke -2 (dari belakang)
# akbar index ke 2 atau ke -1 (dari belakang)
# contoh mau ambil data :
print(data[0])

# menghitung panjang data, menggunakan len
print(len(data)) #output 3, karena pada list "data" ada 3 elemen

# manipulasi list
# menambah data
print(f'data sebelum ditambah = \n{data}')
# data.insert(posisi,item)
data.insert(0,"abdurrasyid")
print(f'data setelah ditambah = \n{data}')
# menambah data di akhir pakai append
data.append("ganteng")
print(f'data tambah append = \n{data}')
# menambah list dengan list
data_baru = ["aa","ii"]
data.extend(data_baru)
print(f'data gabungan = \n{data}')

#MERUBAH DATA
data[-1] = "gentos" # ii diganti jadi gentos
print (f'data ubah = \n{data}')

#mendelete data
data.remove("aa")
print (f'data remove = \n{data}')

# menghilangkan data yg paling akhir
data.pop()
print(f"data akhir hilang= \n{data}")

