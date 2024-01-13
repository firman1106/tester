
data = "ini adalah string" #kumpulan karakter
print(data)
print(type(data))

# cara buat string
# 1. menggunakan single quote
data = 'ini single quote'
print(data)
# 2. menggunakan double quote
data = "ini double quote"
print(data)
# 3. menggunaka tanda \
# data = 'sekarang hari jum'at'
# (ini error karena di kata jum'at ada quote terdetek)
data = 'sekarang hari jum\'at'
print(data)
# gunakan slash untuk mengatasinya
#bagimana jika mau ngetik gini:
# C:\User\Firman , slash nya kedetek error, maka
data = 'C:\\User\\Firman'
print(data)

#pakai tab (jauhan)
data = "Firman\t\t\tMaulana\tAkbar"
print(data)

#backspace (jadi deketan)
data = 'Firman \bMaulana'
print(data)

#newline (nge enter)
data = 'baris pertama\nbaris kedua'
print(data)

#menggunakan string literal atau raw
#akan bermasalah jika:
data = "C:\new folder" #harus dibetulkan pakai raw
data = r"C:\new folder"
#pakai r jadi semua kata akan terdetek sbagai string
#walaupun biasanya terdetek rumus \n \t \b 
print(data)

# multi line literal string
print ("""
apapaun yang tertulis diantara 3x double quote,
maka akan terbaca sebagai string, apapun yyaaa
       """)
# multiline literal string dan raw
print (r"""ini sama aja yaa 
misal, www.abdurrasyid.com/newID""")