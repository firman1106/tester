def average(list_data):
    print(f'mencari average dari {list_data}')
    print(f'sum-nya = {sum(list_data)}')
    print(f'len-nya = {len(list_data)}')
    print(f'averagenya = sum / len')
    print(f'averagenya = {sum(list_data)} / {len(list_data)}')
    print(f'averagenya = {sum(list_data)/len(list_data)}\n')

a = [1,2,3,4,5]
b = [12,23,34,45,56]
c = [34,656,2]
d = [11,22,33,44]

average(a)
average(b)
average(c)
average(d)

print('\nKalkulator Temperature dari Celcius')
def kalkulator_dari_C(nilai_celcius):
    #dari C ke R rumusnya: R = (4/5)*C
    reamur = (4/5)*nilai_celcius
    print(f'{nilai_celcius} Celcius = {reamur} Reamur')
    #dari C ke F rumusnya: ((9/5)*C)+32
    fahrenheit = ((9/5)*nilai_celcius)+32
    print(f'{nilai_celcius} Celcius = {fahrenheit} Fahrenheit')
    #dari C ke K rumusnya: C+273
    kelvin = nilai_celcius + 273
    print(f'{nilai_celcius} Celcius = {kelvin} Kelvin\n')

kalkulator_dari_C(0)
kalkulator_dari_C(45)
kalkulator_dari_C(20)

print('\nKalkulator Temperature dari Reamur')
def kalkulator_dari_R(nilai_reamur):
    #dari R ke C rumusnya: C = (5/4)*R
    celcius = (5/4)*nilai_reamur
    print(f'{nilai_reamur} Reamur = {celcius} Celcius')
    #dari R ke F rumusnya: ((9/4) * R + 32
    fahrenheit = ((9/4) * nilai_reamur) + 32
    print(f'{nilai_reamur} Reamur = {fahrenheit} Fahrenheit')
    #dari R ke K rumusnya: ((5/4) * R) + 273
    kelvin = ((4/5) * nilai_reamur) + 273
    print(f'{nilai_reamur} Reamur = {kelvin} Kelvin\n')

kalkulator_dari_R(0)
kalkulator_dari_R(45)
kalkulator_dari_R(20)

print('\nKalkulator Temperature dari Fahrenheit')
def kalkulator_dari_F(nilai_fahrenheit):
    #dari F ke C rumusnya: (5/9) * (F - 32)
    celcius = (5/9) * (nilai_fahrenheit - 32)
    print(f'{nilai_fahrenheit} Fahrenheit = {celcius} Celcius')
    #dari F ke R rumusnya: (4/9) * (F - 32)
    fahrenheit = (4/9) * (nilai_fahrenheit - 32)
    print(f'{nilai_fahrenheit} Fahrenheit = {fahrenheit} Reamur')
    #dari F ke K rumusnya: ((5/9) * (F-32)) + 273
    kelvin = ((5/9) * (nilai_fahrenheit-32)) + 273
    print(f'{nilai_fahrenheit} Fahrenheit = {kelvin} Kelvin\n')

kalkulator_dari_F(0)
kalkulator_dari_F(45)
kalkulator_dari_F(20)

print('\nKalkulator Temperature dari Kelvin')
def kalkulator_dari_K(nilai_kelvin):
    #dari K ke C rumusnya: K - 273
    celcius = nilai_kelvin - 273
    print(f'{nilai_kelvin} Kelvin = {celcius} Celcius')
    #dari K ke R rumusnya: (4/5) * (K - 273)
    reamur = (4/5) * (nilai_kelvin - 273)
    print(f'{nilai_kelvin} Kelvin = {reamur} Reamur')
    #dari K ke F rumusnya: ((9/5) * (K - 273)) + 32
    fahrenheit = (4/5) * (nilai_kelvin - 273)
    print(f'{nilai_kelvin} Kelvin = {fahrenheit} Fahrenheit\n')

kalkulator_dari_K(0)
kalkulator_dari_K(45)
kalkulator_dari_K(20)

print("\nMuanntaaps Luuurd")

def convert_temperature(degrees,from_unit,to_unit):
    fahrenheit_formula = 5/9*(degrees-32)
    celcius_formula = ((9/5)*degrees)+32
    kelvin_formula = degrees - 273
    if from_unit == "F":
        print(f"{degrees}C = {fahrenheit_formula} F")
    elif from_unit == "C":
        print(f"{degrees}F = {celcius_formula} C")
    elif from_unit == "K":
        print(f"{degrees}C = {kelvin_formula} K")
    else :
        print("None of that is true")


convert_temperature(10,"K","C")