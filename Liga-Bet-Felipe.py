# Liga-BeyPlay-Felipe
# =========================
# GESTION LIGA BETPLAY
# =========================

equipos = {}


# =========================
# FUNCION REGISTRAR EQUIPO
# =========================

def registrar_equipo():

    nombre = input("Nombre del equipo: ")
    ciudad = input("Ciudad: ")

    equipos[nombre] = {
        "ciudad": ciudad,

        "estadisticas": {
            "PJ": 0,
            "PG": 0,
            "PP": 0,
            "PE": 0,
            "GF": 0,
            "GC": 0,
            "TP": 0
        },

        "cuerpo_tecnico": {
            "director_tecnico": "",
            "preparador_fisico": "",
            "medico": "",
            "fisioterapeuta": ""
        },

        "jugadores": []
    }

    print(" Equipo registrado correctamente..")


# =========================
# REGISTRAR CUERPO TECNICO
# =========================

def registrar_cuerpo_tecnico():

    equipo = input("Equipo: ")

    if equipo in equipos:

        equipos[equipo]["cuerpo_tecnico"]["director_tecnico"] = input("Director tecnico: ")
        equipos[equipo]["cuerpo_tecnico"]["preparador_fisico"] = input("Preparador fisico: ")
        equipos[equipo]["cuerpo_tecnico"]["medico"] = input("Medico: ")
        equipos[equipo]["cuerpo_tecnico"]["fisioterapeuta"] = input("Fisioterapeuta: ")

        print(" Cuerpo tecnico registrado")

    else:
        print(" Equipo no existe")


# =========================
# REGISTRAR JUGADOR
# =========================

def registrar_jugador():

    equipo = input("Equipo: ")

    if equipo in equipos:

        jugador = {
            "nombre": input("Nombre jugador: "),
            "nacionalidad": input("Nacionalidad: "),
            "posicion": input("Posicion: "),
            "dorsal": input("Numero dorsal: "),
            "edad": input("Edad: ")
        }

        equipos[equipo]["jugadores"].append(jugador)

        print(" Jugador agregado")

    else:
        print(" Equipo no encontrado")


# =========================
# REGISTRAR PARTIDO
# =========================

def registrar_partido():

    local = input("Equipo local: ")
    visitante = input("Equipo visitante: ")

    if local in equipos and visitante in equipos:

        goles_local = int(input(f"Goles de {local}: "))
        goles_visitante = int(input(f"Goles de {visitante}: "))

        # PARTIDOS JUGADOS
        equipos[local]["estadisticas"]["PJ"] += 1
        equipos[visitante]["estadisticas"]["PJ"] += 1

        # GOLES
        equipos[local]["estadisticas"]["GF"] += goles_local
        equipos[local]["estadisticas"]["GC"] += goles_visitante

        equipos[visitante]["estadisticas"]["GF"] += goles_visitante
        equipos[visitante]["estadisticas"]["GC"] += goles_local

        # GANADOR
        if goles_local > goles_visitante:

            equipos[local]["estadisticas"]["PG"] += 1
            equipos[local]["estadisticas"]["TP"] += 3

            equipos[visitante]["estadisticas"]["PP"] += 1

            print(f" Ganó {local}")

        elif goles_visitante > goles_local:

            equipos[visitante]["estadisticas"]["PG"] += 1
            equipos[visitante]["estadisticas"]["TP"] += 3

            equipos[local]["estadisticas"]["PP"] += 1

            print(f" Ganó {visitante}")

        else:

            equipos[local]["estadisticas"]["PE"] += 1
            equipos[visitante]["estadisticas"]["PE"] += 1

            equipos[local]["estadisticas"]["TP"] += 1
            equipos[visitante]["estadisticas"]["TP"] += 1

            print(" Empate..")

    else:
        print(" Uno de los equipos no existe")


# =========================
# MOSTRAR TABLA
# =========================

def mostrar_tabla():

    print("\n======= TABLA =======")

    for equipo, datos in equipos.items():

        e = datos["estadisticas"]

        print(f"""
Equipo: {equipo}
PJ: {e['PJ']}
PG: {e['PG']}
PP: {e['PP']}
PE: {e['PE']}
GF: {e['GF']}
GC: {e['GC']}
TP: {e['TP']}
---------------------
""")


# =========================
# MOSTRAR JUGADORES
# =========================

def mostrar_jugadores():

    equipo = input("Equipo: ")

    if equipo in equipos:

        for jugador in equipos[equipo]["jugadores"]:

            print(f"""
Nombre: {jugador['nombre']}
Nacionalidad: {jugador['nacionalidad']}
Posicion: {jugador['posicion']}
Dorsal: {jugador['dorsal']}
Edad: {jugador['edad']}
----------------------
""")

    else:
        print(" Equipo no encontrado")


# =========================
# MENU
# =========================

while True:

    print("""
========= LIGA BETPLAY =========

1. Registrar equipo
2. Registrar cuerpo tecnico
3. Registrar jugador
4. Registrar partido
5. Mostrar tabla
6. Mostrar jugadores
7. Salir

================================
""")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_equipo()

    elif opcion == "2":
        registrar_cuerpo_tecnico()

    elif opcion == "3":
        registrar_jugador()

    elif opcion == "4":
        registrar_partido()

    elif opcion == "5":
        mostrar_tabla()

    elif opcion == "6":
        mostrar_jugadores()

    elif opcion == "7":
        print(" Saliendo...")
        break

    else:
        print(" Opcion invalida")