import psycopg2 as p
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
            num = float(input("Número:"))
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
    if opcion == 1:
        archivo = open("Prog1.txt", "a")

        print("Primer Número")
        uno = pedir_numero()
        print("Segundo Número")
        dos = pedir_numero()
        print("Tercer Número")
        tres = pedir_numero()
        uno1 = str(uno)
        dos2 = str(dos)
        tres3 = str(tres)
        archivo.write("El primer número es:" + uno1);
        archivo.write("\n");
        archivo.write("El segundo número es:" + dos2);
        archivo.write("\n");
        archivo.write("El tercer número es:" + tres3);
        archivo.write("\n");
        if (tres == dos) and (tres != uno):
            print("El número: ",uno," es diferente\n")
            archivo.write("El número " + uno1+" es diferente")
            archivo.write("\n")
            archivo.write("\n")
        elif (uno>dos) and (uno>tres):
            resultado=uno+dos+tres
            print("La suma es:",resultado)
            print()
            resultado1=str(resultado)
            archivo.write("La suma es:" + resultado1);
            archivo.write("\n");
            archivo.write("\n");
        elif (tres == uno) and (dos != uno):
            print("El número: ",dos," es diferente\n")
            archivo.write("El número " + dos2+" es diferente")
            archivo.write("\n")
            archivo.write("\n")
        elif (dos>uno) and (dos>tres):
            resultadoo=uno*dos*tres
            print("La multiplicación es:", resultadoo)
            print()
            resultadoo1=str(resultadoo)
            archivo.write("La multiplicación es:" + resultadoo1);
            archivo.write("\n");
            archivo.write("\n");
        elif (dos == uno) and (tres != uno):
            print("El número: ",tres," es diferente\n")
            archivo.write("El número " + tres3+" es diferente")
            archivo.write("\n")
            archivo.write("\n")
        elif (tres>uno) and (tres>dos):
            print(uno,",",dos,",",tres)
            print()
            archivo.write(uno1 + "," + dos2 + "," +tres3);
            archivo.write("\n");
            archivo.write("\n");

        else:
            print("Todos son iguales")
            archivo.write("Todos son iguales");
            archivo.write("\n");
            archivo.write("\n");
        archivo.close()
    elif opcion == 2:
        salir = True
    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')