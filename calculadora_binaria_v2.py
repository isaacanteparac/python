import os
from antcer import xuduosofy
array_ente = []
array_fracciona = []
array_binario = []
contador, presicion,mant,exp,signo = 0,0,0,0,0
texto_arc = open('texto_bin.txt','w')



def menu():
    global presicion,exp,mant,contador,signo
    os.system('cls')
    array_ente.clear()
    array_fracciona.clear()
    array_binario.clear()
    exp,mant,presicion,contador,signo = 0,0,0,0,0
    print()
    print("     [CALCULADORA BINARIA]")
    print()
    print("1: IEEE-751 de 32bits(precision simple,decimal fracciomario)")
    print("2: IEEE-754 de 64bits(precision doble,decimal fracciomario)")
    print("3: IEEE-754 de 128bits(precision cuadruple,decimal fracciomario)")
    print("4: Conversion de binario a decimal(binario entero)")
    print("5: Conversion a CA1 y CA2 (binario entero)")
    print("6: Conversion de hexadecimal a binario")
    print("7: Conversion de binario a hexadecimal")
    print("8: Traducido de texto a binario")
    print("10: Salir")
    while True:
        try:
            print()
            opcion = int(input("Ingrese opcion: "))
            print()
        except:
            menu()
            continue
        if opcion == 1:
            presicion = 127
            exp = 8
            mant = 23
            ieee("SIMPLE 32BITS")
        elif opcion == 2:
            presicion = 1023
            exp = 11
            mant = 52
            ieee("DOBLE 64BITS")
        elif opcion == 3:
            presicion = 16383
            exp = 15
            mant = 122
            ieee("CUADRUPLE 128BITS")
        elif opcion == 4:
            os.system('cls')
            decimal_binario(2)
        elif opcion == 5:
            ca1_ca2()
        elif opcion == 6:
            hexa_bina()
        elif opcion == 7:
            bina_hexa()
        elif opcion == 8:
            tex_bina()
        elif opcion == 10:
            os.system('cls')
            print('© 2020 XUDUOSOFT, CORP.')
            exit()
        else:
            menu()




def ieee(nom):
    global signo
    os.system('cls')
    print()
    print(f"<IEEE-754 PRESICION {nom} XXX.YY>")
    print()
    while True:
        try:
            signo = str(input("Ingrese el signo: "))
        except:
            ieee(nom)
            continue
        if signo == str("-"):
            signo = 1
        elif signo == str("+"):
            signo = 0
        else:
            ieee(nom)
        num_origi = float(input("Ingrese el numero decimal fraccionario: "))
        num_origi = str(num_origi)
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
        print(f"Entero      {array_ente[contador][i]}/2 = bits {array_ente[contador+1][i]}")
    array_ente[contador+1].reverse()
    print(f"Resultado       {array_ente[contador+1]}")
    suma = (longi-1)+precision
    if contador == 1:
        print(f"Recorrido de punto hasta el primer entero {longi-1}")
        print(f"Suma de recorrido {longi-1}+{precision} = {suma}")
        multipli_ieee()
    contador +=1
    if contador == 4:
        print()
        mostrar_ieee()
        input("Pulse enter para ir al menu...")
        menu()
    division_ieee(suma)



def decimal_binario(num):
    os.system('cls')
    print()
    print("<CONVERSION DE BINARIO A DECIMAL>")
    print()
    bina = str(input("Ingrese binario entero: "))
    array_binario.append([])
    for i in range(len(bina)):
        ente=int(bina[i])
        array_binario[0].append(ente)
    print(f"Binario = {array_binario[0]}")
    print()
    array_binario[0].reverse()
    for i in range(len(array_binario[0])):
        decimal = (num**i)*array_binario[0][i]
        array_binario[0].append(decimal)
        print(f"Potencia = ({num}^{i})*{array_binario[0][i]} = {decimal}")
        print()
    print(f"Total decimal = {sum(array_binario[0])}")
    input("Pulse enter para ir al menu...")
    menu()



def multipli_ieee():
    print()
    print("_____MULTIPLICAION______")
    array_fracciona[1].append(array_fracciona[0][0])
    log = 0
    mult = array_fracciona[1][log]*2
    print(f"Decimal     {array_fracciona[1][0]} * 2 = {mult}")
    array_fracciona[1].append(mult)
    for _i in range(7):
        mult = str(mult)
        m = mult.split('.')
        array_fracciona[2].append(f"0.{m[1]}")
        array_fracciona[2][log] = float(array_fracciona[2][log])
        mult = array_fracciona[2][log]*2
        array_fracciona[1].append(mult)
        print(f"Decimal     {array_fracciona[2][log]} * 2 = {array_fracciona[1][-1]}")
        log +=1
    for i in range(len(array_ente[2])):
        array_fracciona[3].append(array_ente[2][i])
    array_fracciona[3].pop(0)
    array_fracciona[1].pop(0)
    for j in range(len(array_fracciona[1])):
        array_fracciona[3].append(int(array_fracciona[1][j]))
        array_fracciona[4].append(int(array_fracciona[1][j]))
    print(f"Resultado  {array_fracciona[4]}")



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
    print(f"Signado = {signo} 1bit")
    print(f"Exponente = {array_ente[4]} {exp}bits")
    print(f"Mantisa = {array_fracciona[3]} {mant}bits")
    print("---------------------------------------")
    print()



def sumar_c2_1():
    array_binario[2][0] = bin(array_binario[2][0]+1)
#SOLUCCIONAR EL PROBLEMA DE LA SUMA DE BINARIO 10101010+1=RESULTADO



def ca1_ca2():
    os.system('cls')
    print()
    print("<CONVERSION A CA1 y CA2>")
    print()
    num = str(input("Ingrese binario entero: "))
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
    print(f"    Original(positivo) {array_binario[0]}")
    print(f"    Invertir(negativo) {array_binario[1]}")
    print("CA2")
    print(f"    Original(positivo) {array_binario[0]}")
    print(f"    Invertir(negativo) {array_binario[1]} + 1= {array_binario[2][0]}")
    print()
    print(array_binario)
    print()
    input("Pulse enter para ir al menu...")
    menu()



def hexa_bina():
    os.system('cls')
    print()
    print("<CONVERSION DE HEXADECIMAL A BINARIO>")
    print()
    hexa = str(input("Ingrese hexadecimal: ")).upper()
    for i in range(len(hexa)):
        array_binario.append([hexa[i]])
        ident_hexa("ex_bi")
        print(f"{array_binario[i][0]} = {array_binario[i][1]}")
    input("Pulse enter para ir al menu...")
    menu()



def ident_hexa(nombre):
    for i in range(len(array_binario)):
        if nombre == str("ex_bi"):
            if array_binario[i][0] == '0':
                array_binario[i].append('0000')
            elif array_binario[i][0] == '1':
                array_binario[i].append('0001')
            elif array_binario[i][0] == '2':
                array_binario[i].append('0010')
            elif array_binario[i][0] == '3':
                array_binario[i].append('0011')
            elif array_binario[i][0] == '4':
                array_binario[i].append('0100')
            elif array_binario[i][0] == '5':
                array_binario[i].append('0101')
            elif array_binario[i][0] == '6':
                array_binario[i].append('0110')
            elif array_binario[i][0] == '7':
                array_binario[i].append('0111')
            elif array_binario[i][0] == '8':
                array_binario[i].append('1000')
            elif array_binario[i][0] == '9':
                array_binario[i].append('1001')
            elif array_binario[i][0] == 'A':
                array_binario[i].append('1010')
            elif array_binario[i][0] == 'B':
                array_binario[i].append('1011')
            elif array_binario[i][0] == 'C':
                array_binario[i].append('1100')
            elif array_binario[i][0] == 'D':
                array_binario[i].append('1101')
            elif array_binario[i][0] == 'E':
                array_binario[i].append('1110')
            elif array_binario[i][0] == 'F':
                array_binario[i].append('1111')
        if nombre == str("bi_ex"):
            if array_binario[i][0] == '0000':
                array_binario[i].append('0')
            elif array_binario[i][0] == '0001':
                array_binario[i].append('1')
            elif array_binario[i][0] == '0010':
                array_binario[i].append('2')
            elif array_binario[i][0] == '0011':
                array_binario[i].append('3')
            elif array_binario[i][0] == '0100':
                array_binario[i].append('4')
            elif array_binario[i][0] == '0101':
                array_binario[i].append('5')
            elif array_binario[i][0] == '0110':
                array_binario[i].append('6')
            elif array_binario[i][0] == '0111':
                array_binario[i].append('7')
            elif array_binario[i][0] == '1000':
                array_binario[i].append('8')
            elif array_binario[i][0] == '1001':
                array_binario[i].append('9')
            elif array_binario[i][0] == '1010':
                array_binario[i].append('A')
            elif array_binario[i][0] == '1011':
                array_binario[i].append('B')
            elif array_binario[i][0] == '1100':
                array_binario[i].append('C')
            elif array_binario[i][0] == '1101':
                array_binario[i].append('D')
            elif array_binario[i][0] == '1110':
                array_binario[i].append('E')
            elif array_binario[i][0] == '1111':
                array_binario[i].append('F')
        if nombre == str("tex_b"):
            if array_binario[i][0] == str("A"):
                array_binario[i][0] = "01000001"
            elif array_binario[i][0] == str("B"):
                array_binario[i][0] = "01000010"
            elif array_binario[i][0] == str("C"):
                array_binario[i][0] = "01000011"
            elif array_binario[i][0] == str("D"):
                array_binario[i][0] = "01000100"
            elif array_binario[i][0] == str("E"):
                array_binario[i][0] = "01000101"
            elif array_binario[i][0] == str("F"):
                array_binario[i][0] = "01000110"
            elif array_binario[i][0] == str("G"):
                array_binario[i][0] = "01000111"
            elif array_binario[i][0] == str("H"):
                array_binario[i][0] = "01001000"
            elif array_binario[i][0] == str("I"):
                array_binario[i][0] = "01001001"
            elif array_binario[i][0] == str("J"):
                array_binario[i][0] = "01001010"
            elif array_binario[i][0] == str("K"):
                array_binario[i][0] = "01001011"
            elif array_binario[i][0] == str("L"):
                array_binario[i][0] = "01001100"
            elif array_binario[i][0] == str("M"):
                array_binario[i][0] = "01001101"
            elif array_binario[i][0] == str("N"):
                array_binario[i][0] = "01001110"
            elif array_binario[i][0] == str("O"):
                array_binario[i][0] = "01001111"
            elif array_binario[i][0] == str("P"):
                array_binario[i][0] = "01001000"
            elif array_binario[i][0] == str("Q"):
                array_binario[i][0] = "01010001"
            elif array_binario[i][0] == str("R"):
                array_binario[i][0] = "01010010"
            elif array_binario[i][0] == str("S"):
                array_binario[i][0] = "01010011"
            elif array_binario[i][0] == str("T"):
                array_binario[i][0] = "01010100"
            elif array_binario[i][0] == str("U"):
                array_binario[i][0] = "01010101"
            elif array_binario[i][0] == str("V"):
                array_binario[i][0] = "01010110"
            elif array_binario[i][0] == str("W"):
                array_binario[i][0] = "01010111"
            elif array_binario[i][0] == str("X"):
                array_binario[i][0] = "01011000"
            elif array_binario[i][0] == str("Y"):
                array_binario[i][0] = "01011001"
            elif array_binario[i][0] == str("Z"):
                array_binario[i][0] = "01011010"



def bina_hexa():
    global  contador
    os.system('cls')
    print()
    print("<CONVERSION DE BINARIO A HEXADECIMAL>")
    print()
    hexa = str(input("Ingrese binario: "))
    if len(hexa)>4:
        contador = len(hexa)//4
        n1 = 0
        n2 = 4
        for _i in range(contador):
            array_binario.append([hexa[n1:n2]])
            n1 +=4
            n2 +=4
    else:
        contador = 1
        array_binario.append([hexa[0:4]])
    ident_hexa("bi_ex")
    print("---------------------------------------")
    for j in range(contador):
        print(f"Hexad    {array_binario[j][0]} = {array_binario[j][1]}")
    print("---------------------------------------")
    print()
    input("Pulse enter para ir al menu...")
    menu()



def val_bit(vari):
    for k in range(len(vari)):
        if vari[k] == '0' or vari[k] == '1':
            print("si cumple")
        else:
            print("no cumple")



def tex_bina():
    global texto_arc
    os.system('cls')
    print()
    print("<TRADUCCION DE TEXTO A BINARIO>")
    print()
    palabras = str(input("Ingrese texto: ")).upper()
    for i in range(len(palabras)):
        array_binario.append([palabras[i]])
    ident_hexa("tex_b")
    for j in range(len(array_binario)):
        for k in range(len(array_binario[j])):
            texto_arc.write(array_binario[j][k])
    texto_arc = open('texto_bin.txt','r')
    print("<Binario>")
    print("---------------------------------------")
    print( texto_arc.read() )
    print("---------------------------------------")
    print()
    input("Pulse enter para ir al menu...")
    menu()


xuduosofy()
menu()
