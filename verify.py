import traceback

def validar_Pan(cadena):
    thirdOperation = 0
    if cadena == "":
        return False
    longCadena = len(cadena)
    if not (longCadena==13 or longCadena==16 or longCadena==19):
        return False

    if longCadena == 16:
        for i in range(longCadena):
            if i%2 == 0 and cadena[i].isdigit() :
                firstOperation = (int(cadena[i:i+1]))*2
                if firstOperation >= 10 and firstOperation < 20 :
                    firstOperation = 1 + firstOperation - 10
                elif firstOperation >= 20 :
                    return False
                secondOperation = firstOperation
                thirdOperation += secondOperation
            
            elif cadena[i].isdigit():
                firstOperation = (int(cadena[i:i+1]))*1
                if firstOperation >=10 and firstOperation < 20:
                    firstOperation = 1 + firstOperation - 10
                elif firstOperation >= 20 :
                    return False
                secondOperation = firstOperation
                if i != len(cadena) - 1 :
                    thirdOperation += secondOperation
            
            else :
                return False
            
        condicion = 1
        for j in range(2,15):
            if thirdOperation == i*10:
                condicion = 0
                break

        fourthOperation = 0

        if condicion == 1 :
            for k in range(2,15):
                a = k*10
                if thirdOperation < a:
                    fourthOperation = a -thirdOperation
                    condicion = 0
                    break

        if condicion == 1 :
            return False

        fifthOperation = str(fourthOperation)
        fifthOperation = fifthOperation[0:1]
        if not (fifthOperation == cadena[len(cadena)-1:len(cadena)]) :
            # print("this false")
            return False

    # print("this true")
    return True


def execution(pan):
    resultado = False
    try:
        resultado = validar_Pan(str(pan))
        print(resultado)
    except:
        traceback.print_exc()
    if not resultado:
        print("************")
        try:
            pan1 = int(pan)
            flag = False
            while not flag :
                pan1 += 1
                if validar_Pan(str(pan1)):
                    flag = True
            print(pan1)
        except:
            traceback.print_exc()

x = input("Pan: ")
execution(x)