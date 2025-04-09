import logging
from torneio.time import Time
from torneio.partida import Partida
from torneio.resultado import ResultadoTorneio

logging.basicConfig(filename='erros.log', level=logging.ERROR)

class Torneio:
    def __init__(self):
        self.times = {}
        self.partidas = []

    def adicionar_time(self, nome):
        try:
            if not nome or not nome.strip():
                raise ValueError("Nome inválido")
            self.times[nome] = Time(nome)
            print(f"✅ Time \"{nome}\" adicionado com sucesso!")
        except Exception as e:
            print(f"❌ Erro: {e}")
            logging.error(f"Erro ao adicionar time: {e}")

    def criar_partida(self, nome1, nome2, gols1, gols2):
        try:
            if nome1 not in self.times or nome2 not in self.times:
                raise ValueError("Time não existe")
            if gols1 < 0 or gols2 < 0:
                raise ValueError("Número inválido de gols")
            time1 = self.times[nome1]
            time2 = self.times[nome2]
            partida = Partida(time1, time2, gols1, gols2)
            self.partidas.append(partida)

            if gols1 > gols2:
                time1.pontos += 3
            elif gols2 > gols1:
                time2.pontos += 3
            else:
                time1.pontos += 1
                time2.pontos += 1

            print(f"✅ Partida entre \"{nome1}\" e \"{nome2}\" criada com sucesso!")
        except Exception as e:
            print(f"❌ Erro: {e}")
            logging.error(f"Erro ao criar partida: {e}")

    def jogar(self):
        return ResultadoTorneio(self.times, self.partidas)
