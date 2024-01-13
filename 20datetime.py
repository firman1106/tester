#date and time

import datetime
print(datetime.date.today())
hari_ini = datetime.date.today()
print(hari_ini)

import datetime as dt 
print(dt.date.today())

tanggal_lahir = dt.date(1999,6,11)
print(tanggal_lahir, "firman lahir")
print(f'firman lahir hari = {tanggal_lahir:%A}')

print(f'\nmasukkan tanggal lahir')
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tanggal_lahir_anda = dt.date(tahun,bulan,tanggal) 
print(f'anda lahir pada: {tanggal_lahir_anda}')
print(f'lahir hari\t: {tanggal_lahir_anda:%A}')

print(f'{5*"="} FIRMAN {5*"="} ')
umur_firman = (hari_ini - tanggal_lahir).days
print(f'Umur firman {int(umur_firman / 365)} Tahun')