import csv
import os
import msvcrt

cin = []
pokes = " "

with open('Python-Clase 11\pokemon_primera_generacion(1).csv', newline='', encoding='utf-8') as f:
    data = csv.reader(f,delimiter=",")
    pokes = list(data)

while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""
         Sistema de selección de Pokemón
    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    1.	Mostrar todos los Pokémon disponibles.
    2.	Buscar un Pokémon por nombre.
    3.	Agregar un Pokémon al cinturón.
    4.	Mostrar los Pokémon en el cinturón.
    5.	Quitar un Pokémon en el cinturón
    6.	Salir.
    """)
    opcion = int(input("Selecxione: "))

    if opcion==1:
        print("Pokémon disponibles")
        for i in range(1,len(pokes)):
            for j in range(len(pokes[i])):
                print(f"{pokes[0][j]}: {pokes[i][j]}")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    elif opcion==2:
        print("Buscar un Pokémon")
        nom = input("Ingrese nombre del Pokemón: ").capitalize()
        centinela = False
        for poke in pokes:
            if poke[1]==nom:
                print("\033[33mPokemón encontrado\033[0m")
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                print(f"Número: {poke[0]}\nNombre: {poke[1]}\nTipo: {poke[2]}\nAltura (m): {poke[3]}\nPeso (kg): {poke[4]}")
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                centinela = True
        if centinela==False:
            print("\033[31mPokemón no encontrado\033[0m")
    elif opcion==3:
        print("Agregar un Pokémon al equipo")
        nom = input("Ingrese nombre del Pokemón: ").capitalize()
        centinela = False
        if len(cin)<6:
            for poke in pokes:
                if poke[1]==nom:
                    print("\033[33mPokemón encontrado\033[0m")
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    print(f"Número: {poke[0]} Nombre: {poke[1]}")
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    centinela = True
                    if not poke[1] in cin:
                        cin.append(poke[1])
                        print("\033[33mPokemón agregado\033[0m")
                    else:
                        print("\033[31mEl Pokemón ya se encuentra en el cinturón de equipo\033[0m")
        if centinela==False:
            print("\033[31mPokemón no encontrado\033[0m")
    elif opcion==4:
        print("Mostrar equipo en el cinturón")
        print("Equipo actual:")
        for i in range(len(cin)):
            print(f"{i+1}.- {cin[i]}")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    elif opcion==5:
        print("Quitar un Pokémon del equipo")
        for i in range(len(cin)):
            print(f"{i+1}.- {cin[i]}")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        nom = input("Ingrese nombre del Pokemón: ").capitalize()
        centinela = False
        for poke in cin:
            if poke[1]==nom:
                print("\033[33mPokemón encontrado\033[0m")
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                print(f"Número: {poke[0]} Nombre: {poke[1]}")
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                centinela = True
                if not poke[1] in cin:
                    cin.append(poke[1])
                    print("\033[33mPokemón agregado\033[0m")
                else:
                    print("\033[31mEl Pokemón ya se encuentra en el cinturón de equipo\033[0m")
        if centinela==False:
            print("\033[31mPokemón no encontrado\033[0m")
    elif opcion==6:
        print("Saliendo")
        break

