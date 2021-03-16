"Determinar que tipo de triángulo es"

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

def pedir_numero_p3():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = float(input("Ingrese lado:"))
            if num>0:
                print()
                correcto = True
            else:
                print("Ingrese un valor positivo\n")
        except ValueError:
            print("Error, Ingrese un número\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar lados")
    print("2. Historial")
    print("3. Salir")
    opcion = pedir_numero_menú()
    archivo = open("Prog1.txt", "a")
    if opcion == 1:
        print("Lado 1")
        l1 = pedir_numero_p3()
        print("Lado 2")
        l2 = pedir_numero_p3()
        print("Lado 3")
        l3 = pedir_numero_p3()
        l11=str(l1)
        l22=str(l2)
        l33=str(l3)
        archivo.write("Lado 1: " + l11);
        archivo.write("\n");
        archivo.write("Lado 2: " + l22);
        archivo.write("\n");
        archivo.write("Lado 3: " + l33);
        archivo.write("\n");
        if (l1==l2) and (l1==l3):
            print("Es un triángulo EQUILATERO\n")
            archivo.write("Es un triángulo EQUILATERO");
            archivo.write("\n");
            archivo.write("\n");
        elif (l1!=l2) and (l2!=l3):
            print("Es un triángulo ESCALENO\n")
            archivo.write("Es un triángulo ESCALENO");
            archivo.write("\n");
            archivo.write("\n");
        else:
            print("Es un triángulo ISÓSCELES\n")
            archivo.write("Es un triángulo ISÓSCELES");
            archivo.write("\n");
            archivo.write("\n");
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
