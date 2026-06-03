# JUEGO INTERACTIVO: LA PRINCESA Y EL DRAGON

input("¡Bienvenido! Ayuda a la princesa a escapar del dragon y encontrar su tesoro de regreso.")
input("La princesa se encuentra en la torre mas alta del castillo, mientras que el dragon esta dormido, la princesa puede BAJAR LAS ESCALERAS , SALIR POR LA VENTANA o BUSCAR LA SALIDA OCULTA.").strip().upper()
decision1 = input("Elige que hara la princesa: ").strip().upper()
if decision1 == "BAJAR LAS ESCALERAS":
    input ("La princesa baja las escaleras, pero el dragon despierta y la atrapa, has perdido")
elif decision1 == "SALIR POR LA VENTANA":
    input ("Ante tan arriesgada decision, el dragon vuela hacia la princesa y la atrapa, has perdido")
elif decision1 == "BUSCAR LA SALIDA OCULTA":
    input ("La princesa encuentra la puerta secreta y escapa de la torre. En la pared del pasadizo encuentra una ANTORCHA, una LINTERNA y un FOSFORO.").strip().upper()
    decision2 = input("¿Cual deberia usar para iluminar el camino?:").strip().upper()
    if decision2 == "ANTORCHA":
        input ("La antorcha ilumina, pero a mitad de camino el humo alerta al dragon y te atrapa, has perdido")
    elif decision2 == "FOSFORO":
        input ("El fosforo se apaga rapidamente y quedas atrapa por siempre en el pasadizo sin luz, has perdido")
    elif decision2 == "LINTERNA":
        input ("La princesa ilumina el final del pasadizo con la linterna y encuentra el mapa para salir del castillo junto a su corona, una de las 4 joyas que ha perdido. El mapa le indica que la segunda joya se encuentra en la habitacion de los guardias, la princesa se dirige hacia alli y encuentra una ESPADA, una TAZA y un ZAPATO.").strip().upper()
        decision3 = input("¿Que objeto deberia usar para enfrentarse a los guardias?:").strip().upper()
        if decision3 == "TAZA":
            input ("La princesa usa la taza para defenderse, pero los guardias se burlan de ella y la atrapan, has perdido")
        elif decision3 == "ZAPATOS":
            input ("Unos zapatos no son utiles para pelear y los guardias te atrapan, has perdido")
        elif decision3 == "ESPADA":
            input ("La princesa se defiende con la espada y derrota a los guardias para llegar hasta la segunda joya, felicidades!. El mapa indica que la tercera joya se encuentra en la biblioteca, la princesa se dirige hacia alli y encuentra un LIBRO, un PIANO y un BOTON.").strip().upper()
            decision4 = input("¿Con que deberia interactuar la princesa?:").strip().upper()
            if decision4 == "BOTON":
                input ("Al presionar el boton, activaste una trampa que te atrapa para siempre, has perdido")
            elif decision4 == "PIANO":
                input ("Al tocar el piano, el sonido alerta al dragon y te atrapa, has perdido")
            elif decision4 == "LIBRO":
                input ("Al abrir el libro, encuentras la tercera joya junto a una llave que abre la puerta de la cueva del dragon dormido, en donde se encuentra la ultima joya. Antes de entrar a la cueva la princesa encuentra una SOGA, una TROMPETA y un ESCUDO.").strip().upper()
                decision5 = input("¿Con que deberia defenderse del dragon la princesa?").strip().upper()
                if decision5 == "TROMPETA":
                    input ("Al tocar la trompeta, el sonido despierta al dragon y te atrapa, has perdido")
                elif decision5 == "SOGA":
                    input ("La soga es muy debil para defenderse y el dragon la rompe, atrapandote, has perdido")
                elif decision5 == "ESCUDO":
                    input ("El escudo te protege ante las llamas del dragon hasta llegar a la ultima joya, ahora debes escapar del castillo con tu tesoro. Puedes SALIR POR LA PUERTA PRINCIPAL, SALTAR AL LAGO O SALTAR AL ABISMO.").strip().upper()
                    decision6 = input("¿Como escapara la princesa?:").strip().upper()
                    if decision6 == "SALIR POR LA PUERTA PRINCIPAL":
                        input ("El dragon ha bloqueado la puerta principal y te atrapa, has perdido")
                    elif decision6 == "SALTAR AL ABISMO":
                        input ("El abismo es muy profundo y no logras sobrevivir, has perdido")
                    elif decision6 == "SALTAR AL LAGO":
                        input ("La princesa salta al lago y nada hasta la orilla, Logrando escapar con su tesoro, ¡Felicidades, has ganado el juego! *inserta creditos*. n_n")
                    else:
                        input ("Opción no válida. Intenta de nuevo.")
                else:
                    input ("Opción no válida. Intenta de nuevo.")
            else:
                input ("Opción no válida. Intenta de nuevo.")
        else:
            input ("Opción no válida. Intenta de nuevo.")
    else:
        input ("Opción no válida. Intenta de nuevo.")
else:
    input ("Opción no válida. Intenta de nuevo.")
