
def pedir_numero_menú():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("\n>Ingrese una opción del menú:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese un número\n")
    return num

def pedir_numero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Número:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese un número\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar números")
    print("2. Salir")

    opcion = pedir_numero_menú()
    if(opcion==1):
        archivo = open("Prog1.txt", "a")
        print("Número inicial")
        inicio = pedir_numero()
        print("Número final")
        final = pedir_numero()
        inicio1=str(inicio)
        final1=str(final)
        if (inicio<=final):
            archivo.write("Número inicial:"+inicio1)
            archivo.write("\n")
            archivo.write("Número final:" + final1)
            archivo.write("\n")
            for n in range(inicio,final+1,2):
                num = str(n)
                print(n)
                archivo.write(num)
                archivo.write("\n")
            archivo.write("\n")
        elif (inicio >= final):
            archivo.write("Número inicial:" + inicio1)
            archivo.write("\n")
            archivo.write("Número final:" + final1)
            archivo.write("\n")
            for n in range(inicio, final - 1, -2):
                num = str(n)
                print(n)
                archivo.write(num)
                archivo.write("\n")
            archivo.write("\n")
            archivo.close()
        else:
            print ("Asegurese que el número de inicial sea menor que el número final")
    elif opcion == 2:
         salir = True
    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')