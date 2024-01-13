# continue, pass

angka = 0
while angka < 5:
    angka += 1
    print(f'angka: {angka}')
    if angka == 3:
        print('okee udah 3 nih, tandain')
        continue
    
    print("itulah angkanyaa")

print('done')