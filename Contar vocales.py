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

def pedir_palabra():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = str(input("Ingrese una palabra o frase:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese una palabra o frase:\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar palabra o frase")
    print("2. salir")

    opcion = pedir_numero_menú()
    if opcion == 1:
        archivo = open("Prog1.txt", "a")
        palabra = pedir_palabra()
        letras=palabra.lower()

        a=letras.count("a")
        e=letras.count("e")
        i=letras.count("i")
        o=letras.count("o")
        u=letras.count("u")
        total=a+e+i+o+u
        total1=str(total)
        print("La palabra",palabra,"tiene",total,"vocales\n")
        archivo.write("La palabra " + palabra + " tiene: "+total1+" vocales.");
        archivo.write("\n");
        archivo.write("\n");
        archivo.close()
    elif opcion == 2:
        salir = True

    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')