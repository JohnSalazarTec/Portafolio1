def contardigitosV3(num):
    if(isinstance(num, int) == False):
        return print("Error tipo de dato, no es entero")
    elif(num == 0):
        return 1
    else:
        return contardigitos_Aux(num)

def contardigitos_Aux(num):
    if(num == 0):
        return 0
    else:
        return 1 + contardigitos_Aux(num // 10)

"""
Nombre:reversaNumero
Entradas:
    n: Entero positivo mayor o igual a cero
salidas:
    Entero mayor a cero que el numero en orden inversa su
    representacion original
Restricciones:
    Entero positivo mayor o igual a cero
"""

def reversaNum(num):
    if isinstance(num, int):
        if (num >= 0):
            if (num <= 10):
                return num
            else:
                return reversaNum_aux(num, contardigitosV3(num))
        else:
            print("El numero debe ser positivo")
    else:
        print ("Error: el numero no es entero")

def reversaNum_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return (num % 10) * (10 ** (largo - 1)) + reversaNum_aux(num // 10, largo - 1)
