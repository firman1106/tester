
#huruf = "abcdefghijklmnopqrstuvwxyz"
#list_huruf = list(huruf)

#nama = (input("masukkan nama: "))
#def count_char(nama):
 #   for i in list_huruf:
  #      jml = nama.count(f'{i}')
 #       if jml > 0:
 #           print(f'{i} : {nama.count(f'{i}')}')



#count_char(nama)
def count_characters(inputnama):
    list_nama = list(inputnama)

    a = dict()

    for i in list_nama:
        a[f"{i}"] = inputnama.count(f'{i}')

    for items in a.items():
	    print(items)


input_nama1 = input("tuliskan nama (1): ")
count_characters(input_nama1)
input_nama2 = input("tuliskan nama (2): ")
count_characters(input_nama2)

list_angka = range(0,10)
for i in list_angka
    if (type(i) == type(0)) == True:
         print(i)
         



list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)