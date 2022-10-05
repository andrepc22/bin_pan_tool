cardNumber = "4120030001409485"
temp = cardNumber[0:(len(cardNumber)-1)]

arreglo = [None]*(len(temp))
arreglo2 = [None]*(len(temp))
# print(arreglo)

for i in range(len(temp)):
    codi = ""+temp[len(temp)-(i+1)]
    arreglo[i] = str.encode(codi)

for i in range(len(arreglo)):
    if i % 2 == 0:
        decodi = arreglo[i]
        arreglo[i] = int(decodi.decode())*2
    else:
        decodi = arreglo[i]
        arreglo[i] = int(decodi.decode())*1

for i in range(len(temp)):
    print(arreglo[i])

for i in range(len(arreglo2)):
    if arreglo[i] > 9:
        arreglo2[i] = arreglo[i] - 9
    else:
        arreglo2[i] = arreglo[i]

for i in range(len(temp)):
    print(arreglo2[i])

sumatoria = 0

for i in range(len(arreglo2)):
    sumatoria += arreglo2[i]

print(sumatoria)

chequeo = ""
if sumatoria % 10 == 0:
    chequeo = "0"
else:
    chequeo = ""+str(10-(sumatoria%10))

print(cardNumber.endswith(chequeo))