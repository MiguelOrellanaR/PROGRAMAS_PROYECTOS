%FACTORIAL
%TAREA 4
%MIGUEL ANTONIO ORELLANA RU�Z
%201801279

clc
clear all
close all
inicio=0;
while inicio==0;
    disp(' ');
    disp(' ');
    disp('------CALCULADORA DE FACTORIAL-------');
    disp('1. Calcular el factorial de un n�mero');
    disp('2. Salir');
    opcion = input('Introduzca la opci�n del men� a realizar : ');
 try
    switch opcion
        case 1, disp('--------------FACTORIAL--------------');
                num =input('Introduzca un n�mero:');
                if num<0
                    fprintf('El factorial de n�meros negativos no existe\n');
                elseif num==0
                fprintf('El factorial de 0 es 1\n');
                else
                factorial=1;
                for i=1:num
                    factorial=factorial*i; 
                end
                fprintf('El resultado del factorial es=: %d \n',factorial);
                end
                archivo = fopen('factorialmat.txt','at');
                fprintf(archivo,'El factorial de %g, es %g \n', num, factorial);
                fclose(archivo);

           case 2, back = input('�Esta seguro que desea salir? s/n: ','s');
            if back=='n' %S�
                inicio=0;
                    clc
            elseif back=='s' %No
            inicio=1;
            end
    end
 catch
        disp('Ingrese un valor correcto')
        Inicio = 1;
end
end