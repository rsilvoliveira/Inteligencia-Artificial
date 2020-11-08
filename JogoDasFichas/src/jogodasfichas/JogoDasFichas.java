package jogodasfichas;

import java.util.ArrayList;
import java.util.Collections;

public class JogoDasFichas {

    static ArrayList<ArrayList<Integer>> estadosGerados = new ArrayList();

    public static void imprimeCaminho(Vertice folha) {
        ArrayList<ArrayList<Integer>> caminho = new ArrayList();
        while (folha != null) {
            caminho.add(folha.getEstado());
            folha = folha.getPai();
        }
        
        for(int i = caminho.size()-1 ; i>-1;i--){
            System.out.println(caminho.get(i));
        }
    }

    public static boolean ehSolucao(ArrayList l, ArrayList solucao) {
        ArrayList<Integer> lCopia = new ArrayList();
        ArrayList<Integer> aux = l;
        ArrayList<Integer> solucaoCopia = new ArrayList();
        ArrayList<Integer> aux2 = solucao;

        for (int i = 0; i < l.size(); i++) {
            lCopia.add(aux.get(i));
            solucaoCopia.add(aux2.get(i));
        }

        return lCopia.equals(solucaoCopia);
    }

    public static void addEstadoGerados(Vertice atual) {
        ArrayList<Integer> aux = new ArrayList();
        for (int i = 0; i < atual.getEstado().size(); i++) {
            aux.add(atual.getEstado().get(i));
        }
        estadosGerados.add(aux);
    }

    public static boolean verificaArvore(Vertice atual) {

        for (int i = 0; i < estadosGerados.size(); i++) {
            if (estadosGerados.get(i).equals(atual.getEstado())) {
                return false;
            }
        }
        return true;
    }

    public static ArrayList<Integer> troca(ArrayList l, int pos) {
        int posVazio = l.indexOf(0);
        Collections.swap(l, posVazio, pos);
        return l;
    }

    public static boolean existeRegra(ArrayList l, int salto, Vertice atual) {
        int posVazio = l.indexOf(0);
        for (int i = posVazio - salto; i <= posVazio + salto; i++) {
            if (i >= 0 && i < l.size()) {
                troca(l, i);
                if (verificaArvore(atual)) {
                    return true;
                } else {
                    troca(l, i);
                }
            }
        }
        return false;
    }

    /* public static void irrevogavel(ArrayList inicio, ArrayList solucao, int salto) {

        Vertice raiz = new Vertice(null, inicio);

        ArrayList<Integer> N = raiz.getEstado();
        boolean fracasso = false, sucesso = ehSolucao(N, solucao);
        Vertice aux = raiz;
        while (fracasso == false && sucesso == false) {
            if (existeRegra(N, salto, aux)) { // HÁ REGRA APLICÁVEL
                //l = regra;
                Vertice aux2 = new Vertice(aux, N);
                aux.addFilho(aux2);
                estadosGerados.add(aux2);
                if (ehSolucao(N, solucao)) {
                    sucesso = true;
                }
                aux = aux2;
            } else {
                fracasso = true;
            }
        }
        System.out.println(N);
        if (fracasso) {
            System.out.println("fracasso");
        }
        if (sucesso) {
            System.out.println("sucesso");
        }
    }*/
    public static void backtraking(ArrayList inicio, ArrayList solucao, int salto) {

        Vertice raiz = new Vertice(null, inicio);

        addEstadoGerados(raiz);

        ArrayList<Integer> S = inicio;

        ArrayList<Integer> N;// = raiz.getEstado();

        boolean fracasso = false, sucesso = false;

        Vertice aux = raiz;

        while (fracasso != true && sucesso != true) {

            //imprimeGerados();

            N = aux.getEstado();

            if (existeRegra(N, salto, aux)) { //R(N) != VAZIO

                addEstadoGerados(aux);

                Vertice aux2 = new Vertice(aux, N);

                aux.addFilho(aux2);

                if (ehSolucao(N, solucao)) {

                    sucesso = true;

                }

                aux = aux2;

            } else {

                if (N == S) {

                    fracasso = true;

                } else {

                    aux = aux.getPai();

                }

            }

        }

        System.out.println("Sucesso: " + sucesso);
        System.out.println("Fracasso: " + fracasso);
        System.out.println(inicio);
        imprimeCaminho(aux);
    }

    /*  public static void buscaLargura(Vertice v, ArrayList solucao) {
        //abertos = Cria uma fila com estados abertos
        Vertice S = v;
        Vertice N = v;
        boolean fracasso = false, sucesso = false;
        //insere S em abertos
        while (!fracasso || !sucesso) {
            if (1 == 1) { //abertos = vazio
                fracasso = true;
            } else {
                //N = primeiro de abertos
                if (ehSolucao(N.getEstado(), solucao)) {
                    sucesso = true;
                } else {
                    while (1 == 1) {//R(N) != VAZIO
                        ///  
                    }
                    ///
                }
            }
        }
    }

    public static void buscaProfundidade(Vertice v, ArrayList solucao) {
        //abertos = Cria uma pilha com estados abertos
        Vertice S = v;
        Vertice N = v;
        boolean fracasso = false, sucesso = false;
        //insere S em abertos
        while (!fracasso || !sucesso) {
            if (1 == 1) { //abertos = vazio
                fracasso = true;
            } else {
                //N = primeiro de abertos
                if (ehSolucao(N.getEstado(), solucao)) {
                    sucesso = true;
                } else {
                    while (1 == 1) {//R(N) != VAZIO
                        ///  
                    }
                    ///
                }
            }
        }
    }

    public static void aEstrela(Vertice v, ArrayList solucao) {
        boolean fracasso = false, sucesso = false;
        Vertice S = v;
        Vertice N;
        //calcule f(S)
        //insere S em abertos (lista)
        //defina fechados
        while (!sucesso || !fracasso) {
            if (1 == 1) { //abertos = vazio
                fracasso = true;
            } else {
                //N = primeiro da lista de abertos - nó com menor f(s)
                if (ehSolucao(N.getEstado(), solucao)) {
                    sucesso = true;
                } else {
                    while (1 == 1) { // R(N) != vazio
                        ///
                    }
                    ///
                }
            }
        }
    }*/
    public static void imprimeGerados() {
        System.out.println("Gerados: " + estadosGerados.size());
        for (int i = 0; i < estadosGerados.size(); i++) {
            System.out.println(estadosGerados.get(i));
        }
    }

    public static void main(String[] args) {

        ArrayList<Integer> I = new ArrayList();

        ArrayList<Integer> S = new ArrayList();

        I.add(1);
        I.add(2);
        I.add(0);
        I.add(2);
        I.add(1);

        S.add(2);
        S.add(2);
        S.add(0);
        S.add(1);
        S.add(1);

        int salto = 2;

        backtraking(I, S, salto);

    }
}
