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
            num = float(input("Puntuación:"))
            if (num >= 0) and (num<=100):
                print()
                correcto = True
            else:
                print("Ingrese una nota dentro del rango")
        except ValueError:
            print("Error, Ingrese una nota valida\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar notas")
    print("2. Historial")
    print("3. salir")
    opcion = pedir_numero_menú()
    archivo = open("Prog1.txt", "a")
    if opcion == 1:
        print("Primera nota")
        n1 = pedir_numero()
        n11=str(n1)
        print("Segunda nota")
        n2 = pedir_numero()
        n22=str(n2)
        print("Tercera nota")
        n3 = pedir_numero()
        n33=str(n3)
        print()
        print("INFORMACIÓN DEL ALUMNO")
        promedio=(n1+n2+n3)/3
        promedio1=str(promedio)
        print("El promedio es:",promedio)
        archivo.write("INFORMACIÓN DEL ALUMNO")
        archivo.write("\n")
        archivo.write("Primera nota: "+n11)
        archivo.write("\n")
        archivo.write("Segunda nota: "+n22)
        archivo.write("\n")
        archivo.write("Tercera nota: "+n33)
        archivo.write("\n")
        archivo.write("El promedio es: "+promedio1)
        archivo.write("\n")
        if (promedio>=60):
            print("APROBADO\n")
            archivo.write("APROBADO")
            archivo.write("\n")
            archivo.write("\n")
        else:
            print ("REPROBADO\n")
            archivo.write("REPROBADO")
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