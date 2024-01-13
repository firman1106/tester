# format str , generic
huruf = "firman"
contoh = f"huruf {huruf}"
print(contoh)

angka = 30
contoh = f"angka {angka}"
print(contoh)

#ribuan atau jutaan
angka=3000
contoh=f"angka {angka:,}"
print(contoh)

angka=2205000
contoh=f"angka {angka:,}"
print(contoh)

#bilangan desimal
angka=200.7987
contoh=f"angka {angka:.2f}"
print(contoh)

angka=200.7987
contoh=f"angka {angka:010.2f}" #leading zero, nol di awal
print(contoh)

#menampilkan tanda + atau -
angka_plus = 5
angka_minus = -5
format_plus = f"plus = {angka_plus:+d}" 
format_minus = f"minus = {angka_minus}"
print(format_plus)
print(format_minus)

#memformat persen %
persen = 0.25
print (f'{persen:%}')

persen = 0.25
print (f'{persen:.2%}') #menampilkan 2 angka dibelakng koma

#melakukan operasi aritmatika di dalam placeholder
sosbak_12 = 27000
qty =13
harga_total= f"Rp {sosbak_12 * qty:,}"
print(harga_total)

# binary, octal, hexadecimal
angka=38
binary = f"binary = {bin(angka)}"
octal = f"octal = {oct(angka)}"
hexadecimal = f"hexadecimal = {hex(angka)}"

print(binary)
print(octal)
print(hexadecimal)