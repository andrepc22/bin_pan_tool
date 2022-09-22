x = input("Bin: ")
y = input("Rango: ")
pan = x+y
print(pan)

def execution():
    
    pass

def digitCheckPan(cardNumber):
    if cardNumber == "" or len(cardNumber) != 13 and len(cardNumber) != 14 and len(cardNumber) != 15 and len(cardNumber) != 16 and len(cardNumber) != 19 :
        return False

    try:
        int(cardNumber)
    except:
        return False

    temp = cardNumber[0:len(cardNumber)-1]
    bt = bytes(len(temp))
    array1, array2 = len(temp), len(temp)

    pass