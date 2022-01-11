class Vertice:

    def __init__(self, pai, estado):
        self.pai = pai
        self.estado = estado
        self.filhos = []
        self.heuristica = 0

    def setPai(self, pai):
        self.pai = pai

    def getPai(self):
        return self.pai

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def addFilho(self, filho):
        self.filhos.append(filho)

    def getFilho(self, i):
        return self.filhos[i]

    def tamanhoFilhos(self):
        return len(self.filhos)

    def setHeuristica(self, h):
        self.heuristica = h

    def getHeuristica(self):
        return self.heuristica