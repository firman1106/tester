#loop (perulangan)

#for kondisi:
#   aksi

#misal kita punya list
angka = [0,1,2,3,4]

for i in angka: #untuk i (elemen list) di dalam angka
    print (f'print elemen i {i}')

#ini dengan range
angka_range = range(5) #membuat semacam list dari 0 - 4 (5 elemen)
for i in angka_range:
    print(f'elemen range {i}')

#ini dengan string
string = "firman maulana akbar"

for huruf in string: # huruf gantinya i, jadi disitu bebas
    print(huruf)