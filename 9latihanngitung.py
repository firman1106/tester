#latihan mengkonversi temperature
#rumusnya :
# R = (4/5)*C
# F = ((9/5)*C)+32 dan ((9/4)*R)+32
# K = C+273 dan ((5/4)*R)+273

print("\nKONVERSI TEMPERATURE\n")
celcius = float(input("masukkan suhu celcius: "))
print("suhu celcius adalah ",celcius,"derajat")

#reamur
reamur = (4/5)*celcius
print(reamur," reamur")

#fahrenheit
fahrenheit = ((9/5)*celcius)+32
print(fahrenheit," fahrenheit")

#kelvin
kelvin = celcius + 273
print(kelvin," kelvin")

# F ke K
print("\nJAWAB PERTANYAAN DI BAWAH INI!")
F = float(input("masukkan nilai Fahrenheit yang akan di convert: "))
print (F,"F berapa K?",)
C = (5/9)*(F-32)
K = ((5/9)*(F-32)) + 273
print("Jawab: ",F," F = ",K," K")

# K ke F
print("\nJAWAB PERTANYAAN DI BAWAH INI!")
K = float(input("masukkan nilai Kelvin yang akan di convert: "))
print (K,"K berapa F?",)
F = ((9/5)*(K - 273))+32
print("Jawab: ",K," K = ",F," F")