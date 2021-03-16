%calculadora en Matlab
inicio=0;
while inicio==0;
disp('caculos matematicos');
disp('1. + SUMA');
disp('2. - RESTA');
disp('3. * MULTIPLICACION');
disp('4. / DIVISION');
opcion = input('OPERACION A EJECTUAR: ');
switch opcion
    case 1, disp('+Suma----------------------------------');
        x = input('ingrese primer numero: ');
        y = input('ingrese segundo numero: ');
        resul = x+y;
        fprintf('resultado=: %d\n',resul);
        back = input('Desea Continuar s/n: ','s');
            if back=='s'
                inicio=0;
                clc
            elseif back=='n'
                inicio=1;
            end
    case 2, disp('-Resta---------------------------------');
        x = input('ingrese primer numero: ');
        y = input('ingrese segundo numero: ');
        resul = x-y;
        %disp('resultado: %d\n',resul);
        fprintf('resultado=: %d\n',resul);
            back = input('Desea Continuar s/n: ','s');
            if back=='s'
                inicio=0;
                clc
            elseif back=='n'
                inicio=1;
            end
    case 3, disp('*Multiplicación------------------------');
        x = input('ingrese primer numero: ');
        y = input('ingrese segundo numero: ');
        resul = x*y;
        %disp('resultado: %d\n',resul);
        fprintf('resultado=: %d\n',resul);
            back = input('Desea Continuar s/n: ','s');
            if back=='s'
                inicio=0;
                clc
            elseif back=='n'
                inicio=1;
            end
    case 4, disp('/División------------------------------');
        x = input('ingrese primer numero: ');
        y = input('ingrese segundo numero: ');
              if y==0
                 disp('Error, division por cero');
              elseif y~=0
                resul = x/y;
                %disp('resultado: %d\n',resul);
                fprintf('resultado=: %d\n',resul);
                back = input('Desea Continuar s/n: ','s');
                    if back=='s'
                    inicio=0;
                    clc
                    elseif back=='n'
                    inicio=1;
                    end
              end
     otherwise, disp('Operación No Valida');
end
end