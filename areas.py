import math

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
            num = float(input("Valor:"))
            if (num > 0):
                correcto = True
            else:
                print("Ingrese un valor positivo\n")
        except ValueError:
            print("Error, Ingrese un número\n")
    return num

salir = False
opcion = 0
while (not salir):
    print("------CALCULADORA DE ÁREAS----")
    print("-------1.Circulo------")
    print("-------2.Triángulo------")
    print("-------3.Cuadrado------")
    print("-------4.Rectángulo------")
    print("-------5.Historial-------")
    print("---------6.Salir---------")
    opcion = pedir_numero_menú()
    archivo = open("Prog1.txt", "a")
    if (opcion == 1):
        print("ÁREA DE UNA CIRCUENFERENCIA")
        archivo.write("ÁREA DE UNA CIRCUENFERENCIA \n")
        print("Ingrese el valor del radio")
        r = pedir_numero()
        r1=str(r)
        archivo.write("El valor del radio ingresado es: "+r1)
        archivo.write("\n")
        area=math.pi * pow(r,2)
        print("El área de la circunferencia es:",area)
        print(" ")
        area1=str(area)
        archivo.write("El valor área es: "+area1)
        archivo.write("\n")
        archivo.write("\n")
    elif (opcion==2):
        print("ÁREA DE UN TRIÁNGULO")
        archivo.write("ÁREA DE UN TRIÁNGULO \n")
        print("Ingrese el valor de la base")
        b=pedir_numero()
        b1=str(b)
        archivo.write("El valor de la base ingresada es: "+b1)
        archivo.write("\n")
        print("Ingrese el valor de la altura")
        h=pedir_numero()
        h1=str(h)
        archivo.write("El valor de la altura ingresada es: "+h1)
        archivo.write("\n")
        area=0.5*b*h
        area1=str(area)
        print("La área del triángulo es:",area)
        print(" ")
        archivo.write("El valor del área es: "+area1)
        archivo.write("\n")
        archivo.write("\n")
    elif (opcion==3):
        print("ÁREA DE UN CUADRADO")
        archivo.write("ÁREA DE UN CUADRADO \n")
        print("Ingrese el valor del lado:")
        l = pedir_numero()
        ll=str(l)
        archivo.write("El valor del lado ingresado es es: "+ll)
        archivo.write("\n")
        area=pow(l,2)
        print("El área del cuadrado es:", area)
        print(" ")
        archivo.write("El valor del área es: "+ll)
        archivo.write("\n")
        archivo.write("\n")
    elif(opcion==4):
        print("ÁREA DE UN RECTÁNGULO")
        archivo.write("ÁREA DE UN RECTÁNGULO \n")
        print("Ingrese el valor de los dos lados diferentes")
        l1=pedir_numero()
        l11=str(l1)
        l2=pedir_numero()
        l22=str(l2)
        archivo.write("El valor del primer lado ingresado es: "+l11)
        archivo.write("\n")
        archivo.write("El valor del segundo lado ingresado es: "+l22)
        archivo.write("\n")
        if (l1!=l2):
            area=l1*l2
            area1=str(area)
            print("El área del rectángulo es:", area)
            print(" ")
            archivo.write("El valor del área es: " + area1)
            archivo.write("\n")
            archivo.write("\n")
        else:
            print("Los lados son iguales, es cuadrado. Hay una opción en el menú para el calculo del área de un cuadrado. \n")
            archivo.close()
    elif opcion == 5:
        archivo = open("Prog1.txt", "r")
        historial = archivo.read()
        archivo.close()
        print(historial)
    elif opcion == 6:
        salir = True

    else:
        print("Ingrese un número que corresponda a una opción del menú\n")

print('   ** Miguel Antonio Orellana Ruíz**')