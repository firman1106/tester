# rumus if:
#if kondisi:aksi

# if in line (satu jalur)
nama = input("aku adalah? ")
if nama=="firman" : print("okee ini Firman, acc")
print(f'Thank\'s {nama}\n')

# if indentation (aksi nya lebih dari satu)
gender = input("whats yout gender? ")
if gender =="female" : #indentation (harus menjorok ke tengah)
    print(f'okee kalo kamu cewe boleh lanjuut')
    nama_cewe = (input("namamu siapaa?"))
    print(f'okee Thank\'s yaa {nama_cewe}')
else:
    print("yaudAH jug close he eh")
