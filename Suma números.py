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
            num = int(input("Ingrese un número entero:"))
            print()
            correcto = True
        except ValueError:
            print("Error, Ingrese un número entero\n")
    return num
salir = False
opcion = 0
while (not salir):
    print('-------MENÚ-------')
    print("1. Ingresar número")
    print("2. salir")

    opcion = pedir_numero_menú()
    if opcion==1:
        archivo = open("Prog1.txt", "a")
        num = pedir_numero()
        num1=str(num)
        archivo.write("El número ingresado es: "+ num1);
        archivo.write("\n");
        if (num>0):
            suma=0
            print("El resultado de la suma")
            temp = []
            for n in range(0,num+1):
                temp.append(str(n))
                suma=suma+n
            f = " + ".join(temp)
            f1=str(f)
            suma1=str(suma)
            print(f," = ",suma)
            print("\n")
            archivo.write(f1)
            archivo.write(" = ")
            archivo.write(suma1)
            archivo.write("\n")
            archivo.write("\n")
        elif (num<0):
            suma = 0
            print("El resultado de la suma")
            temp = []
            for n in range(0, num - 1, -1):
                temp.append(str(n))
                suma = suma + n
            f = "".join(temp)
            f1 = str(f)
            suma1 = str(suma)
            print(f,"=",suma)
            print("\n")
            archivo.write(f1)
            archivo.write("=")
            archivo.write(suma1)
            archivo.write("\n")
            archivo.write("\n")
            archivo.close()
        else:
            print("El número ingresado es cero\n")
    elif opcion == 2:
        salir = True

    else:
        print("Ingrese un número que corresponda a una opción del menú\n")


print('   ** Miguel Antonio Orellana Ruíz**')
