# x = input("Bin: ")
# y = input("Rango: ")
# pan = x+y
pan = input("Pan: ")
print(pan)

def execution(pan):
    isOk = digitCheckPan(pan)
    t = int(pan)
    stop = False

    if isOk :
        print("La tarjeta " + pan + " es correcta")
        while True :
            t += 1
            stop = digitCheckPan(str(t))
            if stop :
                break
        print(t)
    else:
        print("La tarjeta " + pan + " no es correcta")

        for i in range(10000000, 100000000) :
            while True :
                t += 1
                stop = digitCheckPan(str(t))
                if stop :
                    break
            print(t)
            stop = False

def digitCheckPan(cardNumber):
    if cardNumber == "" or len(cardNumber) != 13 and len(cardNumber) != 14 and len(cardNumber) != 15 and len(cardNumber) != 16 and len(cardNumber) != 19 :
        return False

    try:
        int(cardNumber)
    except:
        return False

    temp = cardNumber[0:(len(cardNumber)-1)]

    arreglo = [None]*(len(temp))
    arreglo2 = [None]*(len(temp))

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

    for i in range(len(arreglo2)):
        if arreglo[i] > 9:
            arreglo2[i] = arreglo[i] - 9
        else:
            arreglo2[i] = arreglo[i]

    sumatoria = 0

    for i in range(len(arreglo2)):
        sumatoria += arreglo2[i]

    chequeo = ""
    if sumatoria % 10 == 0:
        chequeo = "0"
    else:
        chequeo = ""+str(10-(sumatoria%10))
    
    return cardNumber.endswith(chequeo)

execution(pan)