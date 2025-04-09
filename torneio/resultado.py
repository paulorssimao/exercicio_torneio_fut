class ResultadoTorneio:
    def __init__(self, times, partidas):
        self.times = times
        self.partidas = partidas

    def imprimir_classificacao(self):
        print("\nClassificação Final:")
        classificados = sorted(self.times.values(), key=lambda t: t.pontos, reverse=True)
        for i, time in enumerate(classificados, 1):
            print(f"{i}. {time.nome} ({time.pontos} pontos)")

    def imprimir_resultados(self):
        print("\nResultados:")
        for partida in self.partidas:
            print(partida.obter_resultado())
