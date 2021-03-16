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

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Mostrar los números impares")
    print("2. Historial")
    print("3. salir")

    opcion = pedir_numero_menú()
    if opcion==1:
        archivo = open("Prog1.txt", "a")
        print("Los números impares del 1 al 100 son:")
        total=0
        for n in range(1,100,2):
            num = str(n)
            print(n)
            archivo.write(num)
            archivo.write("\n")
            total=total+1
            total1=str(total)
        print("La cantidad de números impares son:",total)
        archivo.write("La cantidad de números impares son:"+total1)
        archivo.write("\n")
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
