import os
array_ente = []
array_fracciona = []
array_binario = []
contador, presicion,mant,exp,signo = 0,0,0,0,0



def menu():
    global presicion,exp,mant,contador,signo
    os.system('cls')
    array_ente.clear()
    array_fracciona.clear()
    array_binario.clear()
    exp,mant,presicion,contador,signo = 0,0,0,0,0
    print()
    print("     <CALCULADORA BINARIA>")
    print("1: IEEE-751 de 32bits(precision simple)")
    print("2: IEEE-754 de 64bits(precision doble)")
    print("3: IEEE-754 de 128bits(precision cuadruple)")
    print("4: binario a decimal")
    print("5: CA1 y CA2 entero")
    print("6: Hexadecimal a binario")
    print("7: Binario a hexadecimal")
    print()
    opcion = int(input("ingrese opcion= "))
    print()
    if opcion == 1:
        presicion = 127
        exp = 8
        mant = 23
        ieee("simple 32bits")
    elif opcion == 2:
        presicion = 1023
        exp = 11
        mant = 52
        ieee("doble 64bits")
    elif opcion == 3:
        presicion = 16383
        exp = 15
        mant = 122
        ieee("cuadruple 128bits")
    elif opcion == 4:
        os.system('cls')
        decimal_binario(2)
    elif opcion == 5:
        ca1_ca2()
    elif opcion == 6:
        hexa_bina()
    elif opcion == 7:
        bina_hexa()



def ieee(nom):
    global signo
    os.system('cls')
    print(f"IEEE-754 precision {nom}")
    while True:
        try:
            signo = str(input("ingrese el signo= "))
        except:
            print("ingrese el signo + o -")
            continue
        if signo == str("-"):
            signo = 1
        elif signo == str("+"):
            signo = 0
        else:
            ieee(nom)
        num_origi = str(input("ingrese el numero decimal= "))
        array_ente.append(num_origi.split('.'))
        for _j in range(5):
            array_fracciona.append([])
        for i in range(len(array_ente[0])):
            array_ente[0][i] = int(array_ente[0][i])
        array_fracciona[0].append(str(f"0.{array_ente[0][1]}"))
        array_fracciona[0][0]= float(array_fracciona[0][0])
        array_ente[0].pop()
        division_ieee(array_ente[0][0])



def division_ieee(entero):
    global contador
    print()
    div = entero/2
    div=int(div) 
    array_ente.append([entero])
    contador +=1
    array_ente[contador].append(div)
    longi = 2
    while True:
        longi +=1
        div = div/2
        div = int(div)
        array_ente[contador].append(div)
        if div == 1:
            print("_____DIVISION_____")
            binario_ieee(longi,presicion)



def binario_ieee(longi,precision):
    global contador
    array_ente.append([])
    for i in range(len(array_ente[contador])):
        if array_ente[contador][i]%2 == 0:
            array_ente[contador+1].append(0)
        else:
            array_ente[contador+1].append(1)
        print(f"ENTERO      {array_ente[contador][i]}/2 = bits {array_ente[contador+1][i]}")
    array_ente[contador+1].reverse()
    print(f"RESULTADO       {array_ente[contador+1]}")
    suma = (longi-1)+precision
    if contador == 1:
        print(f"recorrido de punto hasta el primer entero {longi-1}")
        print(f"suma de recorrido {longi-1}+{precision} = {suma}")
        multipli_ieee()
    contador +=1
    if contador == 4:
        print()
        mostrar_ieee()
        input("pulse enter para ir al menu...")
        menu()
    division_ieee(suma)



def decimal_binario(num):
    bina = str(input("ingrese binario = "))
    array_binario.append([])
    for i in range(len(bina)):
        ente=int(bina[i])
        array_binario[0].append(ente)
    print(f"binario = {array_binario[0]}")
    print()
    array_binario[0].reverse()
    for i in range(len(array_binario[0])):
        decimal = (num**i)*array_binario[0][i]
        array_binario[0].append(decimal)
        print(f"potencia = ({num}^{i})*{array_binario[0][i]} = {decimal}")
        print()
    print(f"total decimal = {sum(array_binario[0])}")
    input("pulse enter para ir al menu...")
    menu()



def multipli_ieee():
    print()
    print("_____MULTIPLICAION______")
    array_fracciona[1].append(array_fracciona[0][0])
    log = 0
    mult = array_fracciona[1][log]*2
    print(f"DECIMAL     {array_fracciona[1][0]} * 2 = {mult}")
    array_fracciona[1].append(mult)
    for _i in range(7):
        mult = str(mult)
        m = mult.split('.')
        array_fracciona[2].append(f"0.{m[1]}")
        array_fracciona[2][log] = float(array_fracciona[2][log])
        mult = array_fracciona[2][log]*2
        array_fracciona[1].append(mult)
        print(f"DECIMAL     {array_fracciona[2][log]} * 2 = {array_fracciona[1][-1]}")
        log +=1
    for i in range(len(array_ente[2])):
        array_fracciona[3].append(array_ente[2][i])
    array_fracciona[3].pop(0)
    array_fracciona[1].pop(0)
    for j in range(len(array_fracciona[1])):
        array_fracciona[3].append(int(array_fracciona[1][j]))
        array_fracciona[4].append(int(array_fracciona[1][j]))
    print(f"RESULTADO  {array_fracciona[4]}")



def mostrar_ieee():
    global contador, signo, exp, mant, presicion
    if  (mant == 23) or (mant == 52) or (mant == 122):
        for k in range(len(array_fracciona[3])):
            k +=1
        ceros = mant-k
        for _p in range(ceros):
            array_fracciona[3].append(0)
    print()
    print("---------------------------------------")
    print(f"signado = {signo} 1bit")
    print(f"exponente = {array_ente[4]} {exp}bits")
    print(f"mantisa = {array_fracciona[3]} {mant}bits")
    print("---------------------------------------")
    print()



def sumar_c2_1():
    array_binario[2][0] = bin(array_binario[2][0]+1)



def ca1_ca2():
    os.system('cls')
    num = str(input("ingrese binario= "))
    for _crear in range(3):
        array_binario.append([])
    array_binario[2].append(int(num))
    for i in range(len(num)):
        array_binario[0].append(int(num[i]))
    for j in range(len(array_binario[0])):
        if array_binario[0][j] == int(1):
            array_binario[1].append(0)
        else:
            array_binario[1].append(1)
    sumar_c2_1()
    print("CA1")
    print(f"    original(positivo) {array_binario[0]}")
    print(f"    invertir(negativo) {array_binario[1]}")
    print("CA2")
    print(f"    original(positivo) {array_binario[0]}")
    print(f"    invertir(negativo) {array_binario[1]} + 1= {array_binario[2][0]}")
    print()
    print(array_binario)
    print()
    input("pulse enter para ir al menu...")
    menu()



def hexa_bina():
    os.system('cls')
    print()
    print("<HEXADECIMAL A BINARIO>")
    print()
    hexa = str(input("ingrese hexadecimal: ")).upper()
    for i in range(len(hexa)):
        array_binario.append([hexa[i]])
        ident_hexa("ex_bi")
        print(f"{array_binario[i][0]} = {array_binario[i][1]}")
    input("pulse enter para ir al menu...")
    menu()



def ident_hexa(nombre):
    for i in range(len(array_binario)):
        if nombre == str("ex_bi"):
            if array_binario[i][0] == '0':
                array_binario[i].append('0000')
            if array_binario[i][0] == '1':
                array_binario[i].append('0001')
            if array_binario[i][0] == '2':
                array_binario[i].append('0010')
            if array_binario[i][0] == '3':
                array_binario[i].append('0011')
            if array_binario[i][0] == '4':
                array_binario[i].append('0100')
            if array_binario[i][0] == '5':
                array_binario[i].append('0101')
            if array_binario[i][0] == '6':
                array_binario[i].append('0110')
            if array_binario[i][0] == '7':
                array_binario[i].append('0111')
            if array_binario[i][0] == '8':
                array_binario[i].append('1000')
            if array_binario[i][0] == '9':
                array_binario[i].append('1001')
            if array_binario[i][0] == 'A':
                array_binario[i].append('1010')
            if array_binario[i][0] == 'B':
                array_binario[i].append('1011')
            if array_binario[i][0] == 'C':
                array_binario[i].append('1100')
            if array_binario[i][0] == 'D':
                array_binario[i].append('1101')
            if array_binario[i][0] == 'E':
                array_binario[i].append('1110')
            if array_binario[i][0] == 'F':
                array_binario[i].append('1111')
        elif nombre == str("bi_ex"):
            if array_binario[i][0] == '0000':
                array_binario[i].append('0')
            if array_binario[i][0] == '0001':
                array_binario[i].append('1')
            if array_binario[i][0] == '0010':
                array_binario[i].append('2')
            if array_binario[i][0] == '0011':
                array_binario[i].append('3')
            if array_binario[i][0] == '0100':
                array_binario[i].append('4')
            if array_binario[i][0] == '0101':
                array_binario[i].append('5')
            if array_binario[i][0] == '0110':
                array_binario[i].append('6')
            if array_binario[i][0] == '0111':
                array_binario[i].append('7')
            if array_binario[i][0] == '1000':
                array_binario[i].append('8')
            if array_binario[i][0] == '1001':
                array_binario[i].append('9')
            if array_binario[i][0] == '1010':
                array_binario[i].append('A')
            if array_binario[i][0] == '1011':
                array_binario[i].append('B')
            if array_binario[i][0] == '1100':
                array_binario[i].append('C')
            if array_binario[i][0] == '1101':
                array_binario[i].append('D')
            if array_binario[i][0] == '1110':
                array_binario[i].append('E')
            if array_binario[i][0] == '1111':
                array_binario[i].append('F')


def bina_hexa():
    global  contador
    os.system('cls')
    print()
    print("<BINARIO A HEXADECIMAL>")
    print()
    hexa = str(input("ingrese binario: "))
    contador= len(hexa)//4
    if len(hexa)>4:
        n1 = 0
        n2 = 4
        for _i in range(contador):
            array_binario.append([hexa[n1:n2]])
            n1 +=4
            n2 +=4
        ident_hexa("bi_ex")
    else:
        print("en proceso")
    ident_hexa("bi_ex")
    print("---------------------------------------")
    for j in range(contador):
        print(f"HEXA    {array_binario[j][0]} = {array_binario[j][1]}")
    print("---------------------------------------")
    print()
    input("pulse enter para ir al menu...")


#poner try cach a l momento de ingresar bits
while():
    menu()
