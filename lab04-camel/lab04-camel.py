
# GAǗLEZ

import random
def main():
    print("Hola amigos, bienvenidos al juego del camello!!!")
    print("Acabas de robar un camello y Los nativos te están persiguido porque quieren su camello de vuelta")
    print("Intenta escapar de estos...")
    condicion = False
    distancia_nativos = -20
    distancia_recorrida = 0
    cantimploras_restantes = 3
    cansancio_camello = 0
    sed = 0
    while not condicion:
        print("A. Beber de la cantimplora")
        print("B. Continuar a velocidad normal")
        print("C. Continuar a máxima velocidad")
        print("D. Pasar la noche")
        print("E. Comprobar el estado de la situación")
        print("Q. Salir")
        print("")
        print("//////////////////////////////////////////////////////////")
        print("")
        opcion = input("Cuál es tu elección? ")
        if opcion.upper() == 'Q':
            condicion = True
            print("Saliste del juego...")

        elif opcion.upper() == 'A':
            if cantimploras_restantes > 0:
                print("Bebiendo un poquito de agua... ")
                cantimploras_restantes -= 1
                sed = 0
            else:
                print("No te queda agua")

        elif opcion.upper() == 'B':
            print("Continuando a velocidad normal... ")
            desplazamiento = random.randint(5, 12)
            distancia_recorrida += desplazamiento
            distancia_nativos += random.randint(7, 14)
            sed += 1
            if random.randint(0, 100) <= 5:
                print("Has encontrado un Oasis!!!!")
                sed = 0
                cansancio_camello = 0
                cantimploras_restantes = 3
            print("Millas recorridas ", desplazamiento)

        elif opcion.upper() == 'C':
            print("Continuando a velocidad máxima... ")
            desplazamiento = random.randint(10, 20)
            distancia_recorrida += desplazamiento
            sed += 1
            print("Millas recorridad ", desplazamiento)
            cansancio_camello += random.randint(1, 3)
            distancia_nativos += random.randint(7, 14)
            if random.randint(0, 100) <= 5:
                print("Has encontrado un Oasis!!!!")
                sed = 0
                cansancio_camello = 0
                cantimploras_restantes = 3

        elif opcion.upper() == 'D':
            print(not "Acampando para pasar la noche... ")
            cansancio_camello = 0
            distancia_nativos += random.randint(7, 14)

        elif opcion.upper() == 'E':
            print("Comprobando estado... ")
            print("distancia que te separa de los nativos ", distancia_recorrida - distancia_nativos)
            print("bebidas restantes ", cantimploras_restantes)
            print("Cansancio del camello ", cansancio_camello)
            print("Ganas de beber agua ", sed)

        if distancia_recorrida >= 200:
            print("has ganado la partida!!!!")
            condicion = True
            break

        if sed > 4:
            print("Tienes mucha sed...")

        elif sed > 6:
            print("Has muerto de sed...")
            condicion = True
            break

        if cansancio_camello > 5:
            print("El camello se está agotando...")

        elif cansancio_camello > 8:
            print("El camello se ha muerto...")
            condicion = True
            break

        if distancia_recorrida - distancia_nativos <= 0:
            print("Has perdido la partida, te ha pillado los nativos")
            condicion = True
            break
        elif distancia_recorrida - distancia_nativos <= 15:
            print("Los Nativos están cerca...")


main()


###
