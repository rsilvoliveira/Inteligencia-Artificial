import time as t
import numpy as np


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


'-----------------------------------------------------------------------------'

estadosGerados = []


def ehSolucao(atual, solucao):

    auxAtual = atual.copy()

    auxSolucao = solucao.copy()

    auxAtual.remove(0)

    auxSolucao.remove(0)

    if(auxAtual == auxSolucao):

        return True

    else:

        return False


def regra(lista, salto):

    aux = lista.copy()

    posVazio = lista.index(0)

    for i in range(posVazio - salto, posVazio + salto + 1):

        if (i >= 0 and i < len(aux)):

            aux[posVazio], aux[i] = aux[i], aux[posVazio]

            if (aux in estadosGerados):

                aux[posVazio], aux[i] = aux[i], aux[posVazio]

            else:
                return i

    return -1


def buscaLargura(inicio, solucao, salto):

    tInicial = t.time()

    raiz = Vertice(None, inicio.copy())

    abertos = []

    fracasso = False

    sucesso = False

    abertos.append(raiz)

    fechados = []

    estadosGerados.append(raiz.getEstado())

    while(fracasso != True and sucesso != True):

        if (len(abertos) == 0):

            fracasso = True

        else:
            aux = abertos[0]

            N = aux.getEstado().copy()

            if (ehSolucao(N, solucao)):

                sucesso = True

            else:

                while (regra(N, salto) != -1):

                    r = regra(N, salto)

                    u = N.copy()

                    posVazio = u.index(0)

                    u[r], u[posVazio] = u[posVazio], u[r]

                    estadosGerados.append(u)

                    aux2 = Vertice(aux, u)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.pop(0)

    tFinal = t.time()

    tempoExecucao = tFinal-tInicial

    if(sucesso):

        nosExpandidos = len(fechados)

        nosVisitados = len(abertos)

        caminho = []

        while (aux != None):

            caminho.append(aux.getEstado())

            aux = aux.getPai()

        return tempoExecucao, caminho[::-1], estadosGerados, nosExpandidos, nosVisitados

    else:

        print("Fracasso!")

    estadosGerados.clear()


def buscaProfundidade(inicio, solucao, salto):

    tInicial = t.time()

    raiz = Vertice(None, inicio.copy())

    abertos = []

    fracasso = False

    sucesso = False

    abertos.append(raiz)

    fechados = []

    estadosGerados.append(raiz.getEstado())

    while(fracasso != True and sucesso != True):

        if (len(abertos) == 0):

            fracasso = True

        else:

            aux = abertos[-1]

            N = aux.getEstado().copy()

            if (ehSolucao(N, solucao)):

                sucesso = True

            else:

                while (regra(N, salto) != -1):

                    r = regra(N, salto)

                    u = N.copy()

                    posVazio = u.index(0)

                    u[r], u[posVazio] = u[posVazio], u[r]

                    estadosGerados.append(u)

                    aux2 = Vertice(aux, u)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.remove(aux)

    tFinal = t.time()

    tempoExecucao = tFinal-tInicial

    if(sucesso):

        nosExpandidos = len(fechados)

        nosVisitados = len(abertos)

        caminho = []

        while (aux != None):

            caminho.append(aux.getEstado())

            aux = aux.getPai()

        return tempoExecucao, caminho[::-1], estadosGerados, nosExpandidos, nosVisitados

    else:

        print("Fracasso!")

    estadosGerados.clear()


def backtrack(inicio, solucao, salto):

    raiz = Vertice(None, inicio.copy())

    estadosGerados.append(raiz.getEstado())

    fracasso = False

    sucesso = False

    aux = raiz

    while(fracasso != True and sucesso != True):

        N = aux.getEstado().copy()

        if(regra(N, salto) != -1):

            r = regra(N, salto)

            u = N.copy()

            posVazio = u.index(0)

            u[r], u[posVazio] = u[posVazio], u[r]

            estadosGerados.append(u)

            aux2 = Vertice(aux, u)

            aux.addFilho(aux2)

            if(ehSolucao(u, solucao)):

                sucesso = True

            aux = aux2

        else:

            if(aux == raiz):

                fracasso = True

            else:

                aux = aux.getPai()

    # if(sucesso):

    #     print("Sucesso!")

    #     while (aux != None):

    #         print(aux.getEstado())

    #         aux = aux.getPai()

    # else:

    #     print("Fracasso!")

    estadosGerados.clear()


def buscaGulosa(inicio, solucao, salto):

    raiz = Vertice(None, inicio.copy())

    estadosGerados.append(raiz.getEstado())

    abertos = []

    fracasso = False

    sucesso = False

    f = h(raiz, solucao)

    raiz.setHeuristica(f)

    abertos.append(raiz)

    fechados = []

    while(fracasso != True and sucesso != True):

        if(len(abertos) == 0):

            fracasso = True

        else:

            j = abertos[0]

            for i in range(len(abertos)):

                if(abertos[i].getHeuristica() < j.getHeuristica()):

                    j = abertos[i]

            aux = j  # no com menor f

            N = aux.getEstado().copy()

            if(ehSolucao(N, solucao)):

                sucesso = True

            else:

                while(regra(N, salto) != -1):

                    r = regra(N, salto)

                    u = N.copy()

                    posVazio = u.index(0)

                    u[r], u[posVazio] = u[posVazio], u[r]

                    estadosGerados.append(u)

                    aux2 = Vertice(aux, u)

                    f = h(aux2, solucao)

                    aux2.setHeuristica(f)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.remove(aux)

    if(sucesso):
        
        print("Sucesso!")
        
        while (aux != None):
            
            print(aux.getEstado())
            
            aux = aux.getPai()
    
    else:
    
        print("Fracasso!")
    
    estadosGerados.clear()


def h(no, solucao):  # numero de fichas fora do lugar

    N = no.getEstado().copy()

    sol = solucao.copy()

    N.remove(0)

    sol.remove(0)

    pecasFora = 0

    for i in range(len(N)):

        if(N[i] != sol[i]):

            pecasFora += 1

    return pecasFora


def criaVetor(tamanho):

    import random

    l1 = []

    l2 = []

    a = tamanho // 2

    for i in range(0, a):

        l1.append(1)

        l2.append(1)

    for i in range(a, 2*a):

        l1.append(2)

        l2.append(2)

    l1.append(0)

    l2.append(0)

    while(l1 == l2):
        random.shuffle(l1)

        random.shuffle(l2)

    return l1, l2


def criaVetorSeq(tamanho):

    l1 = []

    l2 = []

    a = tamanho // 2

    for i in range(0, a):

        l1.append(1)

        l2.append(2)

    l1.append(0)

    l2.append(0)

    for i in range(a, 2*a):

        l1.append(2)

        l2.append(1)

    return l1, l2


'-----------------------------------------------------------------------------'

tamanho = 51

salto = 40

tempos = []

ini = t.time()

for i in range(1):

    inicio, solucao = criaVetorSeq(tamanho)

    tInicial = t.time()

    # backtrack(inicio, solucao, salto)

    # buscaLargura(inicio, solucao, salto)

    # buscaProfundidade(inicio, solucao, salto)

    buscaGulosa(inicio, solucao, salto)

    tFinal = t.time()

    tempos.append(tFinal-tInicial)


f = t.time()

print("Min:", min(tempos))

print("Max:", max(tempos))

print("Média:", np.mean(tempos))

print()

print("Total:", f-ini, "s")
