import Algoritmos as a
import time as t

tamanho = 5

salto = 2

"Vetores totalmente aleatorio"
inicio, solucao = a.criaVetor(tamanho)

"Vetores seq. Ex.: 1,1,0,2,2 e 2,2,0,1,1"
inicioSeq, solucaoSeq = a.criaVetorSeq(tamanho)

print()

print("Inicio:", inicioSeq)

print("Solução:", solucaoSeq)

print()

i = t.time()

a.backtrack(inicioSeq,solucaoSeq,salto)

# a.buscaLargura(inicioSeq, solucaoSeq, salto)

# a.buscaProfundidade(inicioSeq,solucaoSeq,salto)

# a.buscaOrdenada(inicioSeq,solucaoSeq,salto)

# a.buscaGulosa(inicioSeq, solucaoSeq, salto)

# a.buscaA(inicioSeq, solucaoSeq, salto)

# a.buscaIDA(inicioSeq, solucaoSeq, salto)

f = t.time()

print()

print("Total",f-i,"s")