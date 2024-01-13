# latihan looping

#menggambar segitiga pakai looping
#mennggunakan for
sisi = 6
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# menggunakan while
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi:
        break
print ("done\n")
count = 1
while True:
    if count % 2:
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
print ("done\n")
