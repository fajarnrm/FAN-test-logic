test = []
i = 0

jumlah = int(input('jumlah bilangan: '))
pasang = 0
while i < jumlah:
    bill = int(input("input %i: "))
    test.append(bill)
    i+=1

j = 0
test.sort()
total = len(test)
jual = []
while j <jumlah:
    test.append(0)
    cek =  test[j]
    if cek == test[j+1]:
        jual.append(cek)
        while cek != test[j+1]:
            if test.count(cek) % 2 == 1:
                pasang-= 1
        pasang+= 1
        j+=1
        
    j+=1

print("total jumlah ada", pasang ,"pasang")
print("Keterangan; Hanya ada", pasang, "pasang kaos kaki yang dapat dijual",jual)

    
