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

# a.backtrack(inicioSeq,solSeq,salto)

# a.buscaLargura(inicioSeq, solSeq, salto)

# a.buscaProfundidade(inicioSeq,solSeq,salto)

a.buscaGulosa(inicioSeq, solucaoSeq, salto)
"Fiz baseado no A* do slide, mas agr n sei se eh o A* ou o guloso"
"Esse eh o mais rápido - dá pra colocar um tamanho muito alto, desde que os saltos sejam bem altos também"
"fiz um teste com tamanho 51 e salto 40, demorou 40s"

f = t.time()

print()

print("Total:", f-i, "s")
