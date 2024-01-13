def convert_degrees(degrees,from_unit,to_unit):
    if from_unit == "C":
        if to_unit == "C":
            print(f'{degrees} Celcius')
        elif to_unit == "R": #dari C ke R rumusnya: R = (4/5)*C
            reamur = (4/5) * degrees
            print(f'{degrees} Celcius = {reamur} Reamur')
        elif to_unit == "F": #dari C ke F rumusnya: ((9/5)*C)+32
            fahrenheit = ((9/5)*degrees)+32
            print(f'{degrees} Celcius = {fahrenheit} Fahrenheit')
        elif to_unit == "K": #dari C ke K rumusnya: C+273
            kelvin = degrees+273
            print(f'{degrees} Celcius = {kelvin} Kelvin')
        else:
            print("Oopps salaahh")
    elif from_unit == "R":
        if to_unit == "R":
            print(f'{degrees} Reamur')
        elif to_unit == "C": #dari R ke C rumusnya: C = (5/4)*R
            celcius = (5/4)*degrees
            print(f'{degrees} Reamur = {celcius} Celcius')
        elif to_unit == "F": #dari R ke F rumusnya: ((9/4) * R + 32
            fahrenheit = ((9/4)*degrees)+32
            print(f'{degrees} Reamur = {fahrenheit} Fahrenheit')
        elif to_unit == "K": #dari R ke K rumusnya: ((5/4) * R) + 273
            kelvin = ((5/4)*degrees)+273
            print(f'{degrees} Reamur = {kelvin} Kelvin')
        else:
            print("Oopps salaahh")
    elif from_unit == "F":
        if to_unit == "F":
            print(f'{degrees} Fahrenheit')
        elif to_unit == "C": #dari F ke C rumusnya: (5/9) * (F - 32)
            celcius = (5/9) * (degrees - 32)
            print(f'{degrees} Fahrenheit = {celcius} Celcius')
        elif to_unit == "R": #dari F ke R rumusnya: (4/9) * (F - 32)
            reamur = (4/9) * (degrees - 32)
            print(f'{degrees} Fahrenheit = {reamur} Reamur')
        elif to_unit == "K": #dari F ke K rumusnya: ((5/9) * (F-32)) + 273
            kelvin = ((5/9) * (degrees-32)) + 273
            print(f'{degrees} Fahrenheit = {kelvin} Kelvin')
        else:
            print("Oopps salaahh")
    elif from_unit == "K":
        if to_unit == "K":
            print(f'{degrees} Kelvin')
        elif to_unit == "C": #dari K ke C rumusnya: K - 273
            celcius = degrees - 273
            print(f'{degrees} Kelvin = {celcius} Celcius')
        elif to_unit == "R": #dari K ke R rumusnya: (4/5) * (K - 273)
            reamur = (4/5) * (degrees - 273)
            print(f'{degrees} Kelvin = {reamur} Reamur')
        elif to_unit == "F": #dari K ke F rumusnya: ((9/5) * (K - 273)) + 32
            fahrenheit = ((9/5) * (degrees - 273)) + 32
            print(f'{degrees} Kelvin = {fahrenheit} Fahrenheit')
        else:
            print("Oopps salaahh")
    else:
        print("Oopps salaahh")

convert_degrees(20,"F","K")