def calcular_estadisticas(rounds):
    estadisticas = {}

    for ronda in rounds:
        puntajes_ronda = {}

        for participante, jueces in ronda['scores'].items():
            puntaje = sum(jueces.values())

            if participante not in estadisticas:
                estadisticas[participante] = {
                    "total": 0,
                    "victorias": 0,
                    "mejor_ronda": 0,
                    "rondas": 0
                }

            estadisticas[participante]["total"] += puntaje
            estadisticas[participante]["rondas"] += 1

            if puntaje > estadisticas[participante]["mejor_ronda"]:
                estadisticas[participante]["mejor_ronda"] = puntaje

            puntajes_ronda[participante] = puntaje

        ganador = max(puntajes_ronda, key=puntajes_ronda.get)
        estadisticas[ganador]["victorias"] += 1

   
    for participante, datos in estadisticas.items():
        datos["promedio"] = round(datos["total"] / datos["rondas"], 1)

    return estadisticas