
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
            num = int(input("Ingrese fecha de nacimiento:"))
            if (num>0) and (num<2021):
                correcto = True
            else:
                print("Ingrese una fecha de nacimiento valida\n")
        except ValueError:
            print("Ingrese una fecha de nacimiento valida\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar fecha de nacimiento")
    print("2. Historial")
    print("3. salir")
    opcion = pedir_numero_menú()
    if opcion == 1:
        archivo = open("Prog1.txt", "a")
        nacimiento = pedir_numero()
        nacimiento1=str(nacimiento)
        archivo.write("La fecha de nacimiento es: "+nacimiento1)
        archivo.write("\n")
        if (nacimiento % 4 == 0):
            print("Nació en un año bisiesto.\n")
            archivo.write("Nació en un año bisiesto.")
            archivo.write("\n")
            archivo.write("\n")
        else:
            print("No nació en un año bisiesto.\n")
            archivo.write("No nació en unaño bisiesto.")
            archivo.write("\n")
            archivo.write("\n")
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