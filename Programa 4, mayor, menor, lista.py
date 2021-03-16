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
            num = int(input("Número:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese un número entero\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar números")
    print("2. salir")
    opcion = pedir_numero_menú()
    if opcion == 1:
        archivo = open("Prog1.txt", "a")
        print("Ingrese el primer número")
        num1 = pedir_numero()
        print("Ingrese el segundo número")
        num2 = pedir_numero()
        num11=str(num1)
        num22=str(num2)
        archivo.write("El primer número es:" + num11);
        archivo.write("\n");
        archivo.write("El segundo número es:" + num22);
        archivo.write("\n");
        if (num1<num2):
            print("El número mayor es:",num2)
            archivo.write("El número mayor es:" + num22);
            archivo.write("\n");
            for n in range(num2,num1-1,-1):
                num = str(n)
                print(n)
                archivo.write(num)
                archivo.write("\n")
            archivo.write("\n")

        elif (num1>num2):
            print("El número mayor es:", num1)
            archivo.write("El número mayor es:" + num11);
            archivo.write("\n");
            for n in range(num1,num2-1,-1):
                num = str(n)
                print(n)
                archivo.write(num)
                archivo.write("\n")
            archivo.write("\n")

        else:
            print ("Los números son iguales")
            archivo.write("Los dos números son iguales");
            archivo.write("\n");
        archivo.write("\n");
        archivo.close()
    elif opcion == 2:
         salir = True

    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')
