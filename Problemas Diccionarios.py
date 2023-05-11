#!/usr/bin/env python3
# -*- coding: utf-8 -*-

creadores="""
Creado por :
Herrera Garcia Ivan - 19130535
Garcia Yescas Fatima Gorety - 19130527
Cordova Palomares Isaias Gerardo - 19130514

PROGRAMA HECHO PARA LA CLASE DE BIG DATA 12:00-13:00
Docente : Lamia Hamdan Medina
"""


"""
Resolucion de los problemas
""" 

    
menu = """
Hola bienvenido a nuestro programa a continuacion, contiene las siguientes funciones :
1) De una lista de 20 elementos :
    - Sumar 
    - Multiplicar
    - Restar
    - Copiar
    - Concatenar el contenido de una lista con otra
    - Salida de 1 a N ( Tu eres quien decide el limite )
    - Cantidad de veces imprimir 'G','N'.
2) Convertir una lista  a una lista de diccionarios.
3) Extraer los elementos de una lista de tuplas.
4) Crear tres diccionarios que contengan numero de control (llave) y nombre (valor). Y convertirlos a un sólo diccionario."
5) ejecutar todas las funciones
0) Salir del programa
"""


salir = False
while salir == False:
    print(creadores)
    print(menu) 
   # opcion == 'f'
    opcion = input("Ingresa una de las opciones anteriores : ")
    if opcion == '1':

        print("\na) Crear una lista de, al menos, 20 elementos. Realice las siguientes actividades:")
        "Sume todos los elementos de una lista"
        lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,11,20]
        print("\tLa lista original es:",lista)

        sumLista = 0 
        for elemento in lista :
            sumLista += elemento
        print ("\n\tLa suma de todos los elementos de la lista es:",sumLista)


        "Multiplique todos los elementos de una lista"
        i = 0
        prod = 1
        while i < len(lista):
            prod = prod * lista[i]
            i +=1
        print("\n\tLa multiplicacion de todos los elementos de la lista es:",prod)


        "Determine el menor y el mayor de los elementos de la lista"
        # Mayor
        mayor = lista[0]
        for elem in range(1,20) :
            if lista[elem] > mayor:
                mayor = lista[elem]
        print("\n\tEl elemento mayor de la lista es:",mayor)
        # Menor
        menor = lista[0]
        for elem in range(1,20) :
            if lista[elem] < menor :
                menor = lista[elem]
        print("\tEl elemento menor de la lista es:",menor)


        print("\n\tRealice una copia de la lista y elimine elementos repetidos");
        listaFinal =[]
        for elemento in lista:
            if elemento not in listaFinal :
                listaFinal.append(elemento)
        print("\n\tLa lista sin valores repetidos es:",listaFinal)


        print("\n\tConectando listas");
        """
        A partir de la siguiente lista ['G', 'N'] concatene con otra 
        """
        lista2 = ['G']
        lista3 = ['N']

        listaCon = lista2+lista3

        print("\t",listaCon)

        "no estoy muy seguro de lo anterior asi que jsjsjs lo hare de otra forma a como entendi el problema"
        listaAB = ['A','B']
        listaGN = ['G','N']
        listaConcatenada = listaGN + listaAB
        print("\t",listaConcatenada)

        "lista de  números [1,.., N] donde N es dado por el usuario o predefinido."

        #numero = 3
        numero = (int(input("\tIngresa un numero : ")))
        listaN = []

        for elemento in range(1,numero+1):
            listaN.insert(elemento,elemento)
        print("\t",listaN)

        " Si N = 4, la salida sería : ['G1', 'N1', 'G2', 'N2',  'G3', 'N3', 'G4', 'N4']"
        #vemos el numero de veces que va a imprimir 
        #N = 5
        N = (int(input("\tCant de veces a imprimir G Y N  : "  )))
        N = N+1
        listaFin = []
        k = 0
        for k in range (1,N): 
            l = str(k)
            listaFin.insert(0,"N"+l)
            listaFin.insert(1,"G"+l)
            k +=1

        nuevaLista = list(reversed(listaFin))
        print("\t",nuevaLista)
        #imprimirSalida()


    elif opcion =='2' :
        print("\nb) Convertir una lista  a una lista de diccionarios.")
        listaNums = [1,2,3,4,5,6]
        listaNombres = ["Luis","Paco","Hugo","Daisy","Mimi","Donald"]
        diccionario={}
        i=1
        for i in range(0,6):
            diccionario[i+1] = {
                "Numero":listaNums[i],
                "Nombre":listaNombres[i]
            }
           
        print(diccionario.values())
        #imprimirSalida()

    elif opcion == '3' :
        print("\nc) Extraer los elementos de una lista de tuplas.")

        tupla =   ("Luis", 100, 100), ("Paco", 89, 95), ("Hugo", 65, 98), ("Donald", 45, 70), ("Daisy", 90, 96)
        num = [0, 1, 2, 3, 4]
        i = 0
        listauno = []
        listados = []
        listatres = []

        for i in num :
                listauno.append(tupla[i][num[0]])
        for i in num :
                listados.append(tupla[i][num[1]])
        for i in num :
                listatres.append(tupla[i][num[2]])
        print(listauno)
        print(listados)
        print(listatres)
        #imprimirSalida()

    elif opcion=='4' :
        print("\nd) Crear tres diccionarios que contengan numero de control (llave) y nombre (valor). Y convertirlos a un sólo diccionario.")

        diccUno  = { 1: "Luis", 2: "Paco" }
        diccDos  = { 3: "Hugo", 4: "Donald"}
        diccTres = { 5: "Daisy", 6: "Mimi"}

        diccionario = {}
        diccionario.update(diccUno)
        diccionario.update(diccDos)
        diccionario.update(diccTres)
        print(diccionario)
        #imprimirSalida()
    elif opcion == '5' :
        print("\na) Crear una lista de, al menos, 20 elementos. Realice las siguientes actividades:")
        "Sume todos los elementos de una lista"
        lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,11,20]
        print("\tLa lista original es:",lista)

        sumLista = 0 
        for elemento in lista :
            sumLista += elemento
        print ("\n\tLa suma de todos los elementos de la lista es:",sumLista)


        "Multiplique todos los elementos de una lista"
        i = 0
        prod = 1
        while i < len(lista):
            prod = prod * lista[i]
            i +=1
        print("\n\tLa multiplicacion de todos los elementos de la lista es:",prod)


        "Determine el menor y el mayor de los elementos de la lista"
        # Mayor
        mayor = lista[0]
        for elem in range(1,20) :
            if lista[elem] > mayor:
                mayor = lista[elem]
        print("\n\tEl elemento mayor de la lista es:",mayor)
        # Menor
        menor = lista[0]
        for elem in range(1,20) :
            if lista[elem] < menor :
                menor = lista[elem]
        print("\tEl elemento menor de la lista es:",menor)


        print("\n\tRealice una copia de la lista y elimine elementos repetidos");
        listaFinal =[]
        for elemento in lista:
            if elemento not in listaFinal :
                listaFinal.append(elemento)
        print("\n\tLa lista sin valores repetidos es:",listaFinal)


        print("\n\tConectando listas");
        """
        A partir de la siguiente lista ['G', 'N'] concatene con otra 
        """
        lista2 = ['G']
        lista3 = ['N']

        listaCon = lista2+lista3

        print("\t",listaCon)

        "no estoy muy seguro de lo anterior asi que jsjsjs lo hare de otra forma a como entendi el problema"
        listaAB = ['A','B']
        listaGN = ['G','N']
        listaConcatenada = listaGN + listaAB
        print("\t",listaConcatenada)

        "lista de  números [1,.., N] donde N es dado por el usuario o predefinido."

        #numero = 3
        numero = (int(input("\tIngresa un numero : ")))
        listaN = []

        for elemento in range(1,numero+1):
            listaN.insert(elemento,elemento)
        print("\t",listaN)

        " Si N = 4, la salida sería : ['G1', 'N1', 'G2', 'N2',  'G3', 'N3', 'G4', 'N4']"
        #vemos el numero de veces que va a imprimir 
        #N = 5
        N = (int(input("\tCant de veces a imprimir G Y N  : "  )))
        N = N+1
        listaFin = []
        k = 0
        for k in range (1,N): 
            l = str(k)
            listaFin.insert(0,"N"+l)
            listaFin.insert(1,"G"+l)
            k +=1

        nuevaLista = list(reversed(listaFin))
        print("\t",nuevaLista)
        #---------------B------------------------------------
        print("\nb) Convertir una lista  a una lista de diccionarios.")
        #---------------C-------------------------------------
        print("\nc) Extraer los elementos de una lista de tuplas.")

        tupla =   ("Luis", 100, 100), ("Paco", 89, 95), ("Hugo", 65, 98), ("Donald", 45, 70), ("Daisy", 90, 96)
        num = [0, 1, 2, 3, 4]
        i = 0
        listauno = []
        listados = []
        listatres = []

        for i in num :
                listauno.append(tupla[i][num[0]])
        for i in num :
                listados.append(tupla[i][num[1]])
        for i in num :
                listatres.append(tupla[i][num[2]])
        print(listauno)
        print(listados)
        print(listatres)
        #-------------------------D----------------------------------
        print("\nd) Crear tres diccionarios que contengan numero de control (llave) y nombre (valor). Y convertirlos a un sólo diccionario.")

        diccUno  = { 1: "Luis", 2: "Paco" }
        diccDos  = { 3: "Hugo", 4: "Donald"}
        diccTres = { 5: "Daisy", 6: "Mimi"}

        diccionario = {}
        diccionario.update(diccUno)
        diccionario.update(diccDos)
        diccionario.update(diccTres)
        print(diccionario)
      
        
    elif opcion == '0' :
        print("Gracias por haber usado nuestro programa :)")
        salir = True
        