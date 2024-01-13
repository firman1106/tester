
def even_square_numbers(n):
    n = n + 1
    angka = range(1,n)
    list_angka = list(angka)
    for i in list_angka : #looping dulu
        if i%2 == 0: #pakai modulus untuk memfilter yg ganjil dan genap
            print(i**2)
            # setiap i yang genap, akan dikuadratkan

print("Coba tes")
even_square_numbers(4)
    # angka genap dari 1 - 4 adl: 2, 4
    # output: 2(kuadrat), 4(kuadrat)
    # output: 4, 16

print("\ntes dua kali")
even_square_numbers(5)
    # angka genap dari 1 - 5 adl: 2, 4
    # output: 2(kuadrat), 4(kuadrat)
    # output: 4, 16

print("\ntes sekali lagi eaa")
even_square_numbers(6)
    # angka genap dari 1 - 6 adl: 2, 4, 6
    # output: 2(kuadrat), 4(kuadrat), 6(kuadrat)
    # output: 4, 16, 36

print("\nn = batas angka yang akan dikuadratkan")
input_n = int(input("silakan masukan nilai n sesuka anda: "))
even_square_numbers(input_n)

print("Muantaaaps")