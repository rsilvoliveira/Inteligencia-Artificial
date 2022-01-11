import Grafo as g
import time as t

"Guarda todos os estados gerados pelo algoritmo"
estadosGerados = []
ramificacao = []
'-----------------------------------------------------------------------------'

"Gera 2 vetores de fichas e embaralha"
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


"Gera 2 vetores de fichas sequenciais. Ex.: 11-22 22-11"
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


"Verifica se o vetor é igual ao objetivo desconsiderando o 'espaço' vazio - retorna um conjunto de soluções"
def ehSolucao(atual, solucao):

    auxAtual = atual.copy()

    auxSolucao = solucao.copy()

    auxAtual.remove(0)

    auxSolucao.remove(0)

    if(auxAtual == auxSolucao):

        return True

    else:

        return False


"Verifica se há regra aplicável"
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


"Heurística - Número de fichas fora do lugar"
def h(no, solucao):

    N = no.getEstado().copy()

    sol = solucao.copy()

    N.remove(0)

    sol.remove(0)

    pecasFora = 0

    for i in range(len(N)):

        if(N[i] != sol[i]):

            pecasFora += 1

    return pecasFora


"Retorna a quantidade média de filhos da árvore"        
def  ramificacaoMedia(raiz):
    
    ramificacaoMediaR(raiz)
    
    r = 0
    
    for i in range(len(ramificacao)):
        
        r+=ramificacao[i]
    
    r = r/len(ramificacao)
    
    return r

def ramificacaoMediaR(raiz):
    
    if raiz.tamanhoFilhos() != 0:
        
        a = []
        
        ramificacao.append(raiz.tamanhoFilhos())
        
        for i in range(raiz.tamanhoFilhos()):
            
           a.append(ramificacaoMediaR(raiz.getFilho(i)))


"Retorna a altura/profundidade máxima da árvore"
def altura(raiz):
    
    if raiz.tamanhoFilhos() == 0:
    
        return 0
    
    a = []
    
    for i in range(raiz.tamanhoFilhos()):
        
       a.append(altura(raiz.getFilho(i)))
    
    return max(a) + 1

def imprimeSolucao(alg, raiz, aux, tempo, tamanho, salto, vizitados, expandidos):

    print("Sucesso!")
         
    print()
        
    print("Ramificação Média:",ramificacaoMedia(raiz))

    print("Altura:",altura(raiz))
        
    print()
        
    print("Caminho:")

    print()

    caminho = []

    while (aux != None):

        caminho.append(aux.getEstado())

        aux = aux.getPai()
            
    caminho = caminho[::-1]

    saida(alg, tamanho, salto, caminho, ramificacaoMedia(raiz), altura(raiz), vizitados, expandidos, tempo)
        
    for i in range(len(caminho)):
            
        print(caminho[i])

def saida(alg,tamanho,salto, caminho, rMedia, altura, vizitados, expandidos, tempo):
    
    arquivo = open('Saida.txt', 'w')
    
    arquivo.write("Algoritmo: " + alg + "\n")
    
    arquivo.write("\n")
    
    arquivo.write("Tamanho: " + str(tamanho))
    
    arquivo.write("\n")
    
    arquivo.write("Salto:   " + str(salto))
    
    arquivo.write("\n\n")
        
    arquivo.write("Ramificação Média:   " + str(rMedia) + "\n")
    
    arquivo.write("Altura/Profundidade: " + str(altura) + "\n")
    
    arquivo.write("Nós vizitados:       " + str(vizitados) + "\n")
    
    arquivo.write("Nós expandidos:      " + str(expandidos) + "\n")
    
    arquivo.write("Tempo Execução:      " + str(tempo) + " s\n\n")
    
    arquivo.write("Solução: " + str(len(caminho)) + " passos.\n")
    
    arquivo.write("\n")
    
    for i in range(len(caminho)):
        
        arquivo.write(str(caminho[i]) + "\n")
        
    arquivo.close()

'-----------------------------------------------------------------------------'


def backtrack(inicio, solucao, salto):
    
    ini = t.time()
    
    raiz = g.Vertice(None, inicio.copy())

    estadosGerados.append(raiz.getEstado())

    fracasso = False

    sucesso = False

    aux = raiz

    while(fracasso != True and sucesso != True):

        N = aux.getEstado().copy()

        if(regra(N, salto) != -1):

            r = regra(N,salto)

            u = N.copy()

            posVazio = u.index(0)

            u[r], u[posVazio] = u[posVazio], u[r]

            estadosGerados.append(u)

            aux2 = g.Vertice(aux, u)

            aux.addFilho(aux2)

            if(ehSolucao(u, solucao)):

                sucesso = True

            aux = aux2

        else:

            if(aux == raiz):

                fracasso = True

            else:

                aux = aux.getPai()

    fim = t.time()

    tempo = fim - ini

    if(sucesso):

        imprimeSolucao('Backtrack',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(estadosGerados))

    else:

        print("Fracasso!")

    estadosGerados.clear()


def buscaLargura(inicio, solucao, salto):

    ini = t.time()    

    raiz = g.Vertice(None, inicio.copy())

    abertos = []

    fracasso = False

    sucesso = False

    abertos.append(raiz)

    fechados = []

    estadosGerados.append(raiz.getEstado())

    while(fracasso != True and sucesso != True):

        aux = abertos[0]

        if (len(abertos) == 0):

            fracasso = True

        else:

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

                    aux2 = g.Vertice(aux, u)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.pop(0)

    fim = t.time()

    tempo = fim - ini

    if(sucesso):

        imprimeSolucao('Busca em Largura',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(fechados))

    else:

        print("Fracasso!")

    estadosGerados.clear()
    


def buscaProfundidade(inicio, solucao, salto):

    ini = t.time()    

    raiz = g.Vertice(None, inicio.copy())

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

                    aux2 = g.Vertice(aux, u)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.remove(aux)

    fim = t.time()

    tempo = fim - ini

    if(sucesso):

        imprimeSolucao('Busca em Profundidade',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(fechados))

    else:

        print("Fracasso!")

    estadosGerados.clear()


def buscaOrdenada(inicio, solucao, salto):

    ini = t.time()    

    raiz = g.Vertice(None, inicio.copy())

    estadosGerados.append(raiz.getEstado())

    abertos = []

    fracasso = False

    sucesso = False

    f = 1

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

                    aux2 = g.Vertice(aux, u)

                    f = 1

                    aux2.setHeuristica(f)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.remove(aux)

    fim = t.time()

    tempo = fim - ini

    if(sucesso):

        imprimeSolucao('Busca Ordenada',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(fechados))
    
    else:
    
        print("Fracasso!")
    
    estadosGerados.clear()


def buscaGulosa(inicio, solucao, salto):

    ini = t.time()    

    raiz = g.Vertice(None, inicio.copy())

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

                    aux2 = g.Vertice(aux, u)

                    f = h(aux2, solucao)

                    aux2.setHeuristica(f)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.remove(aux)

    fim = t.time()

    tempo = fim - ini

    if(sucesso):

        imprimeSolucao('Busca Gulosa',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(fechados))
    
    else:
    
        print("Fracasso!")
    
    estadosGerados.clear()

    
def buscaA(inicio, solucao, salto):
    
    ini = t.time()
    
    raiz = g.Vertice(None, inicio.copy())

    estadosGerados.append(raiz.getEstado())

    abertos = []

    fracasso = False

    sucesso = False

    f = h(raiz, solucao) + 1 #Peso unitário

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

                    aux2 = g.Vertice(aux, u)

                    f = h(aux2, solucao) + 1 # Peso unitário

                    aux2.setHeuristica(f)

                    aux.addFilho(aux2)

                    abertos.append(aux2)

                fechados.append(aux)

                abertos.remove(aux)
    
    fim = t.time()

    tempo = fim - ini
    
    if(sucesso):

        imprimeSolucao('Busca A*',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(fechados))
    
    else:
    
        print("Fracasso!")
    
    estadosGerados.clear()
    
    
def buscaIDA(inicio, solucao, salto):
    
    ini = t.time()
    
    fracasso = False
    
    sucesso = False
    
    raiz = g.Vertice(None, inicio.copy())
    
    estadosGerados.append(raiz.getEstado())
    
    f = h(raiz, solucao) + 1
    
    patamar = f
    
    patamar_old = -1
    
    descartados = []
    
    aux = raiz
    
    while(sucesso != True and fracasso != True):
        
        # print(patamar,patamar_old)
        
        N = aux.getEstado().copy()
        
        if(patamar == patamar_old):
            
            fracasso = True
            
        else:
            
            if(ehSolucao(N, solucao) and f <= patamar):
                
                sucesso = True
                
            else:
                
                if(f > patamar):
                    
                    descartados.append(f)
                    
                    aux = aux.getPai()

                if(regra(N, salto)!=-1 ):
                        
                    r = regra(N, salto)
                        
                    u = N.copy()

                    posVazio = u.index(0)

                    u[r], u[posVazio] = u[posVazio], u[r]

                    estadosGerados.append(u)

                    aux2 = g.Vertice(aux, u)
                        
                    f = h(aux2,solucao) + 1
                    
                    aux.addFilho(aux2)
                        
                    aux = aux2
                        
                else:
                        
                    if(N == inicio):
                            
                        patamar_old = patamar
                            
                        patamar = min(descartados) 
                        
                        estadosGerados.clear()
                        
                        estadosGerados.append(inicio)
                            
                    else:
                            
                        aux = aux.getPai()
                 
    fim = t.time()

    tempo = fim - ini
                        
    if(sucesso):

        imprimeSolucao('Busca IDA*',raiz,aux,tempo,len(inicio),salto,len(estadosGerados),len(descartados))
    
    else:
    
        print("Fracasso!")
    
    estadosGerados.clear()