
sw = True
def suma(n1,n2):
    su = n1 + n2
    print(f"La suma es :{su}")
def resta(n1,n2):
    re = n1 - n2
    print(f"La resta es:{re}")
def multiplicacion(n1,n2):
    prod = n1 * n2
    print(f"La multiplicacion es:{prod}")
def division(n1,n2):
    div = n1 / n2
    print(f"La division es :{div}")
def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False
def opcion_no_disponible():
    print('Opcion no disponible')


menu = """
    == == == == = Calculadora == == == ==
    1. Multiplicacion
    2.Division 
    3.Suma
    4.Resta
    5.Salir"""
while sw:
    print(menu)
    op= int(input("Seleccionar una opcion:"))
    if  op==1:
        n1 = float(input("Ingrese numero 1:"))
        n2 = float(input("Ingrese numero 2:"))
        multiplicacion(n1,n2)
    elif op==2:
        n1 = float(input("Ingrese numero 1:"))
        n2 = float(input("Ingrese numero 2:"))
        division(n1,n2)
    elif op==3:
        n1 = float(input("Ingrese numero 1:"))
        n2 = float(input("Ingrese numero 2:"))
        suma(n1,n2)
    elif op==4:
        n1 = float(input("Ingrese numero 1:"))
        n2 = float(input("Ingrese numero 2:"))
        resta(n1,n2)
    elif op==5:
         terminar_programa()
    else:
        opcion_no_disponible()
