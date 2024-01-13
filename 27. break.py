# break

angka = 0
while angka < 5:
    angka += 1
    print(f'angka: {angka}')
    if angka == 3:
        print('okee udah 3 nih, tandain')
        break
    
    print("itulah angkanyaa")

print('done\n')

data_int = int(input("hitung sampai: "))
angka = 0
while True:
    angka += 1
    print(f'hitungan ke {angka}')

    if angka == data_int:
        print ("okee cukup")
        break
print("donee")