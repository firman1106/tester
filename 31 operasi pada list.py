data_angka = [2,3,4,1,3,2,3,4,3,7,6]
print(f'data angka= \n{data_angka}')

#count data
print(f'jumlah data 3 pada data angka ada: {data_angka.count(3)}')

#ambil posisi data
data = ["firman","maulana","akbar"]
print(f'index firman adl: {data.index("firman")}')

#mengurutkan list
print(f'data angka sebelum di sort \n{data_angka}')
data_angka.sort()
print(f'coba di sort: \n{data_angka}')

#kalo mau sort dari belakang berarti setelah sort lakukan reverse
data_angka.reverse()
print(f'data sort dari belakang (reverse): \n{data_angka}')