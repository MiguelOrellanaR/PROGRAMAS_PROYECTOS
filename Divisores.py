def pedir_numero_menú():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("\n>Ingrese una opción del menú:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese un número que corresponda a una opción del menú\n")
    return num

def pedir_numero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Ingrese un número para mostrar sus divisores:"))
            if (num>0):
                correcto = True
            else:
                print("Ingrese un valor entero positivo\n")
        except ValueError:
            print("Error, Ingrese un número entero positivo\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar número")
    print("2. Salir")

    opcion = pedir_numero_menú()
    if opcion==1:
        archivo = open("Prog1.txt", "a")
        div = pedir_numero()
        if (div <= 0):
            print("Ingrese un número entero positivo")
        else:
            print("Los divisores son: ")

            for n in range(1, div + 1):
                if div % n == 0:
                    print(n)
                    num = str(n)
                    archivo.write(num)
                    archivo.write("\n")
        archivo.write("Son los divisores de "+num)
        archivo.write("\n")
        archivo.write("\n")
        archivo.close()
        print()
    elif opcion == 2:
        salir = True
    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')


