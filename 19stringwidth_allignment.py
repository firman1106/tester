#width and multiline

nama = "Firman Maulana Akbar"
umur = 24
tinggi = 165.0
nosepatu = 42

#string
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, no sepatu = {nosepatu}"
print(5*"="+"DATA STRING"+5*"=")
print(data_string)

#string multiline
data_string = f"nama = {nama},\numur = {umur},\ntinggi = {tinggi},\nno sepatu = {nosepatu}"
print(5*"="+"DATA STRING"+5*"=")
print(data_string)

# menggunakan string multiline (kutip triplets)
print("\n" + 5*"="+"DATA STRING"+5*"=")
nama = "Firman"
data_string = f"""
nama   = {nama}
tinggi = {int(tinggi)}
umur   = {umur}

"""
print(data_string)
#coba supaya rata kanan, :>7 untuk rata kanan total 7 char
data_string = f"""
nama   = {nama:>7}
tinggi = {int(tinggi):>7}
umur   = {umur:>7}

"""
print(data_string)
