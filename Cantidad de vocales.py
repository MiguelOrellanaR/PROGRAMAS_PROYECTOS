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

def pedir_palabra():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = str(input("Ingrese una palabra o frase:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese una palabra o frase\n")
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
        palabra= pedir_palabra()
        letras=palabra.lower()

        a=letras.count("a")
        e=letras.count("e")
        i=letras.count("i")
        o=letras.count("o")
        u=letras.count("u")
        a1=str(a)
        e1=str(e)
        i1=str(i)
        o1=str(o)
        u1=str(u)
        print("La palabra o frase ",palabra,"tiene:")
        print("A=",a)
        print("E=",e)
        print("I=",i)
        print("O=",o)
        print("U=",u)
        archivo.write("La palabra o frase " + palabra + " tiene:")
        archivo.write("\n");
        archivo.write("A="+a1)
        archivo.write("\n")
        archivo.write("E="+e1)
        archivo.write("\n")
        archivo.write("I="+i1)
        archivo.write("\n")
        archivo.write("O="+o1)
        archivo.write("\n")
        archivo.write("U="+u1)
        archivo.write("\n")
        archivo.write("\n")
        archivo.close()
    elif opcion == 2:
        salir = True

    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')
