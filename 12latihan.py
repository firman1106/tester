
inputUser = (float(input("masukkan nilai <5 / >10: ")))
isikurangdr5 = (inputUser < 5)
print("kurang dari 5", isikurangdr5)
isilebihdr10 = (inputUser >10)
print ("lebih dari 10", isilebihdr10)

jawaban = isikurangdr5 or isilebihdr10
print("jawaban anda: ", jawaban)

print("\nsoal baru: lebih dr 5 kurang dr 10 ")
inputUser = (float(input("masukkan lebih dr 5 kurang dr 10: ")))
lebihdr5 = (inputUser > 5)
kurangdr10 = (inputUser < 10)
jawaban = lebihdr5 and kurangdr10
print("jawaban anda adalah ", jawaban)

print("\nKerjakan soal ini!")
print("1. ---0+++5---8+++11---\n2. +++0---5+++8---11+++\nJawab:")
inputUser = (float(input("1. masukan jawaban anda: ")))
krg0 = (inputUser >= 0, inputUser < 5, inputUser !>= 5, inputUser !< 8 ) 

print(krg0)

jawab1 = krg0 and krg5 and krg8 and krg11 and lbh11
print("jawaban anda adalah: ", jawab1)
inputUser = (float(input("2. masukan jawaban anda: ")))
isikrg0 = True
isikrg5 = False
isikrg8 = True
isikrg11 = False
isilbh11 = True
jawab2 = isikrg0 or isikrg5 or isikrg8 or isikrg11 or isilbh11
print("jawaban anda adalah: ", jawab2)