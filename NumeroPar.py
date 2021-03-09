"""
Nombre:numeroPar
Entradas:
    n: Entero positivo mayor o igual a cero
salidas:
    Entero mayor a cero donde el numero sea elegido verdadero si es par
    o sea elegido falso si es impar.
Restricciones:
    Entero positivo mayor o igual a cero
"""


def numeroPar(num):
    if(isinstance(num,int)and num>0):
        if(num%2==0):
            return True
        else:
            return False
    else:
        return 'Digite un numero entero'
