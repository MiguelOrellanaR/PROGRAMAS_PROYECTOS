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
            num = int(input("Información:"))
            if (num>0):
                correcto = True
            else:
                print("Ingrese un valor correcto. Verifique que existan carros con esa condición\n")
        except ValueError:
            print("Error, ingrese valores correctos\n")
    return num

salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar datos del taxi")
    print("2. Historial")
    print("3. salir")

    opcion = pedir_numero_menú()
    if opcion==1:
        archivo = open("Prog1.txt", "a")
        print("Ingrese modelo del taxi")
        modelo = pedir_numero()
        modelo1=str(modelo)
        print("Ingrese kilometraje del taxi")
        kilometraje = pedir_numero()
        kilometraje1=str(kilometraje)
        archivo.write("INFORMACIÓN DEL VEHÍCULO")
        archivo.write("\n")
        archivo.write("El vehículo es modelo: "+modelo1)
        archivo.write("\n")
        archivo.write("Tiene "+ kilometraje1+" kilometros recorridos.")
        archivo.write("\n")
        if (modelo<2007) and (kilometraje>20000):
            print("Necesita renovarse\n")
            archivo.write("Necesita renovarse")
            archivo.write("\n")
            archivo.write("\n")
        elif (modelo>=2007) and (modelo<=2013) and (kilometraje<=20000) and (kilometraje>=10000):
            print("Necesita mantenimiento\n")
            archivo.write("Necesita mantenimiento")
            archivo.write("\n")
            archivo.write("\n")
        elif (modelo>2013) and (modelo<=2021) and (kilometraje<10000):
            print("Óptimas condiciones\n")
            archivo.write("Óptimas condiciones")
            archivo.write("\n")
            archivo.write("\n")
        else:
            print("Mecánico")
            archivo.write("Mecánico\n")
            archivo.write("\n")
            archivo.write("\n")
    elif opcion == 2:
        archivo = open("Prog1.txt", "r")
        historial = archivo.read()
        archivo.close()
        print(historial)
    elif opcion==3:
        salir = True

    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')