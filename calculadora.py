"1-suma, 2-resta, 3-multiplicacion, 4-division"
def calculadora(num1, num2, opt):
    print('Bienvenido a la calculadora de Python with fjmurillov3743'.center(50, '-'))
    if opt == 1:
        print(f'El resultado de la suma de {num1} y {num2}: {num1 + num2}')
        
    elif opt == 2:
        print(f'El resultado de la resta de {num1} y {num2} : {num1 - num2}')

    elif opt == 3:
        print(f'El resultado de la multiplicacion {num1} y {num2} : {num1 * num2}')

    elif opt == 4:
        print(f'El resultado de la division {num1} y {num2} : {num1 / num2}')
    else:
        print('Te equivocaste de Opcion: ')

varible1 = float(input('Digite el primer valor: '))
variable2 = float(input('Digite el sugundo valor: '))
calculadora(varible1, variable2,1)
calculadora(varible1, variable2,2)
calculadora(varible1, variable2,3)
calculadora(varible1, variable2,4)

