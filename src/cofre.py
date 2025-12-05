from multiprocessing.spawn import spawn_main

from src.item import Item
from src.moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volumeMaximo = volumeMaximo
        self.volumeAtual = 0
        self.itens = []
        self.moedas = []
        self.estadoCofre = True

    def getVolume(self):
        return self.volumeAtual

    def getVolumeMaximo(self):
        return self.volumeMaximo

    def getVolumeRestante(self):
        return self.getVolumeMaximo() - self.getVolume()

    def add(self, item: Item):
        if self.getVolume() < self.getVolumeMaximo():
            if self.estadoCofre:
                if item.get_volume() <= self.getVolumeRestante():
                    self.itens.append(item.get_descricao())
                    self.volumeAtual += item.get_volume()
                    return True
                return False
            return False
        return False

    def add(self, moeda: Moeda):
        if self.getVolume() < self.getVolumeMaximo():
            if self.estadoCofre:
                if moeda.get_volume() <= self.getVolumeRestante():
                    self.moedas.append(moeda)
                    self.volumeAtual += moeda.get_volume()
                    return True
                return False
            return False
        return False

    def obterItens(self):
        valor = ""
        if self.estadoCofre == False:
            if len(self.itens) > 0:
                for i in range(len(self.moedas)):
                    valor += self.itens[i].get_descricao()
                    return valor
            return "vazio"
        return None

    def obterMoedas(self):
        valor2 = 0
        if self.estadoCofre == False:
            if len(self.moedas) > 0:
                for i in range(len(self.moedas)):
                    valor2 += self.moedas[i].get_valor()
                return valor2
            elif len(self.moedas) == 0:
                return 0
        else:
            return -1

    def taInteiro(self):
        if self.estadoCofre == True:
            return True
        else:
            return False

    def quebrar(self):
        if self.estadoCofre == True:
            self.estadoCofre = False
            return True
        else:
            return False