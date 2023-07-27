x = input("Ingresa el resultado del RBA: ")

def quitar_llaves1(input_string):
    output_string = ""
    for character in input_string:
        if character not in ["{", "}", "[", "]", "(", ")",","]:
            output_string += character
        elif character in ["{", "("]:
            output_string += ""
        elif character in ["}", "[", "]", ")"]:
            output_string += "\n"
        elif character in [","]:
            pass
    return output_string

y = quitar_llaves1(x)
print("\n----------------------------------------------------------------------\n")
print(y)

def quitar_comas(input_string):
    output_string = ""
    for character in input_string:
        if character not in [","]:
            output_string += character
        elif character in [","]:
            output_string += "\n"
    return output_string

#z = quitar_comas(x)
#print("\n----------------------------------------------------------------------\n")
#print(z)