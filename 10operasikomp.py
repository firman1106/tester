#operasi komparasi, hasilnya selalu boolean.. operasinya:
# >, <, >=, <=, ==, !=, is, is not

a = 20
b = 2.1
c = 20
d = 12

# > lebih besar dari, < Lebih kecil dari
tes = a>b
print(tes)

# sama dengan ==
hasil = a==20
print(hasil)
hasil = a==20
print(hasil)

# tidak sama dengan
hasil = a!=20
print(hasil)
hasil=a!=b
print(hasil)

# is dan is not, mengenal id
print(hex(id(c)))
print(hex(id(d)))
banding = c is a
print("c adalah a ", banding)