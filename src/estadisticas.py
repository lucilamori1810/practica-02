def procesar_rondas(rounds):
    estadisticas = {}

    for ronda in rounds:
        print("Ronda:", ronda['theme'])

        puntajes_ronda = {}

        for participante, jueces in ronda['scores'].items():
            puntaje = sum(jueces.values())

            if participante not in estadisticas:
                estadisticas[participante] = {
                    "puntaje_total": 0,
                    "rondas_ganadas": 0,
                    "mejor_ronda": 0,
                    "cantidad_rondas": 0,
                }

            estadisticas[participante]["puntaje_total"] += puntaje
            estadisticas[participante]["cantidad_rondas"] += 1

            if puntaje > estadisticas[participante]["mejor_ronda"]:
                estadisticas[participante]["mejor_ronda"] = puntaje

            puntajes_ronda[participante] = puntaje

        ganador = max(puntajes_ronda, key=puntajes_ronda.get)
        estadisticas[ganador]["rondas_ganadas"] += 1

        print("Ganador:", ganador)
        print("-" * 40)

        calcular_promedios(estadisticas)
        ordenados = ordenar_resultados(estadisticas)
        mostrar_tabla(ordenados)

    return estadisticas


def calcular_promedios(estadisticas):
    for participante, datos in estadisticas.items():
        datos["promedio"] = round(
            datos["puntaje_total"] / datos["cantidad_rondas"], 1
        )
    return estadisticas


def ordenar_resultados(estadisticas):
    return sorted(
        estadisticas.items(),
        key=lambda x: x[1]["puntaje_total"],
        reverse=True
    )


def mostrar_tabla(ordenados):
    print("Tabla final:")
    print("Cocinero | Puntaje total | Rondas ganadas | Mejor ronda | Promedio")

    for participante, datos in ordenados:
        print(
            participante,
            "|",
            datos["puntaje_total"],
            "|",
            datos["rondas_ganadas"],
            "|",
            datos["mejor_ronda"],
            "|",
            datos["promedio"]
        )