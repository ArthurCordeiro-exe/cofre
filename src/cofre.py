from cofre.src.item import Item
from cofre.src.moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volumeMaximo = volumeMaximo
        self.volumeAtual = 0
        self.volumeRestante = self.volumeMaximo - self.volumeAtual
        self.itens = []
        self.moedas = []
        self.estadoCofre = True

    def getVolume(self):
        return self.volumeAtual

    def getVolumeMaximo(self):
        return self.volumeMaximo

    def getVolumeRestante(self):
        return self.volumeRestante

    def add(self, item: Item):
        if self.getVolume() < self.getVolumeMaximo():
            if self.estadoCofre == True:
                if item.get_volume() <= self.getVolumeRestante():
                    self.itens.append(item)
                    self.volumeAtual += item.get_volume()
                    self.volumeRestante -= item.get_volume()
                    return True
                elif item.get_volume() > self.getVolumeRestante():
                    return False
            else:
                return False
        elif self.getVolume() == self.getVolumeMaximo():
            return False
        else:
            return False

    def add(self, moeda: Moeda):
        return True

    def obterItens(self):
        if self.estadoCofre == False:
            if len(self.itens) > 0:
                return self.itens
            elif len(self.itens) == 0:
                return "Vazio"
        else:
            return "Cofre não está quebrado"

    def obterMoedas(self):
        if self.estadoCofre == False:
            if len(self.moedas) > 0:
                return self.moedas
            elif len(self.moedas) == 0:
                return "Vazio"
        else:
            return "Cofre não está quebrado"

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