# list bisa berupa
#Number, string, boolean,
data_number = [1,2,3,4]
data_string = ["firman","maulana","akbar"]
data_boolean = [True, False, False, True]
data_campuran = [1,2,"campur",False]

#cara alternatif membuat list
# pakai range
data_range = range(0,10) # menjadi urutan number
list_range = list(data_range) #di ubah dulu ke list
print(list_range)

# pakai range
data_range = range(0,10,2) # menjadi urutan number (start, stop, step)
list_range = list(data_range) #di ubah dulu ke list
print(list_range)

#menggunakan for loop (list comprehension)
list_comp = [i for i in range(0,10)]
print(list_comp)

list_comp = [i**2 for i in range(0,10)]
print(list_comp)