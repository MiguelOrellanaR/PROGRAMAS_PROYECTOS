
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
            num = int(input("Ingrese número:"))
            if (num >= 0):
                print()
                correcto = True
            else:
                print("Los factoriales de números negativos están indefinidos. Ingrese un entero positivo")
            print()
        except ValueError:
            print("Error, Ingrese un número entero positivo.\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar número")
    print("2. Historial")
    print("3. salir")
    opcion = pedir_numero_menú()
    if opcion == 1:
        archivo = open("Prog1.txt", "a")
        fac = pedir_numero()
        factorial=1
        fac1=str(fac)
        archivo.write("El número ingresado es: " + fac1);
        archivo.write("\n");
        if (fac % 7 ==0):
            for n in range(fac):
                factorial = factorial * (n + 1)
            factorial1=str(factorial)
            print("El factorial es: ", factorial)
            print()
            archivo.write("El factorial es: 1"+factorial1);
            archivo.write("\n");
            archivo.write("\n")
        else:
            print("Error. Ingrese un número divisible entre 7.\n")
            archivo.write("No es un número divisible entre 7.");
            archivo.write("\n");
            archivo.write("\n")
        archivo.close()
    elif opcion == 2:
        archivo = open("Prog1.txt", "r")
        historial = archivo.read()
        archivo.close()
        print(historial)
    elif opcion == 3:
        salir = True
    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')