#logika dan boolean
#not, or, and, xor

# ======NOT======
print("-----NOT")
a = True
c = not a
print("data a = ",a)
print("data c = ",c)
# pakai not selalu menjadi kebalikannya antara:
# true dan false

#======OR=======
print("-----OR")
a = False
b = False
c = a or b
print('a = ',a)
print('b = ',b)
print('a or b = ',c)

a = False
b = True
c = a or b
print('a = ',a)
print('b = ',b)
print('a or b = ',c)

a = True
b = False
c = a or b
print('a = ',a)
print('b = ',b)
print('a or b = ',c)

a = True
b = True
c = a or b
print('a = ',a)
print('b = ',b)
print('a or b = ',c)

# jadi, or ini akan true apabila salah satu atau
# keduanya ada yang true

#======and=======
print("\n----and")
a = False
b = False
c = a and b
print('a = ',a)
print('b = ',b)
print('a and b = ',c)

a = False
b = True
c = a and b
print('a = ',a)
print('b = ',b)
print('a and b = ',c)

a = True
b = False
c = a and b
print('a = ',a)
print('b = ',b)
print('a and b = ',c)

a = True
b = True
c = a and b
print('a = ',a)
print('b = ',b)
print('a and b = ',c)
# jadi, and ini akan true apabila keduanya true

#======xor=======
print("\n----xor")
a = False
b = False
c = a ^ b
print('a = ',a)
print('b = ',b)
print('a xor b = ',c)

a = False
b = True
c = a ^ b
print('a = ',a)
print('b = ',b)
print('a xor b = ',c)

a = True
b = False
c = a ^ b
print('a = ',a)
print('b = ',b)
print('a xor b = ',c)

a = True
b = True
c = a ^ b
print('a = ',a)
print('b = ',b)
print('a xor b = ',c)
# jadi, xor ini akan true apabila salahsatu true
# salahsatu ya, kalo keduanya jadi false