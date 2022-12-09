kalimat = []
cek = int(input("Masukan jumlah kata yang ingin diinputkan: "))
i = 0
count = 0
while i < cek:
    kata = str(input("masukan kata: "))
    kalimat.append(kata)
    i+=1
    if (kata.isalpha()) == True:
        count+=1
print("Jumlah kata yang tidak memiliki karakter spesial = ",count)
