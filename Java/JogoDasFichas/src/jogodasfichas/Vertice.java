package jogodasfichas;

import java.util.ArrayList;
import java.util.List;

public class Vertice {

    private Vertice pai;
    private ArrayList<Integer> estado = new ArrayList<>();
    private ArrayList<Vertice> filhos = new ArrayList<>();

    public Vertice(Vertice pai, List<Integer> estado) {
        this.pai = pai;
        this.estado.addAll(estado);
    }

    public Vertice getPai() {
        return pai;
    }

    public void setPai(Vertice pai) {
        this.pai = pai;
    }

    public ArrayList<Integer> getEstado() {
        return estado;
    }

    public void setEstado(ArrayList<Integer> estado) {
        this.estado = estado;
    }

    public ArrayList<Vertice> getFilhos() {
        return filhos;
    }

    public void setFilhos(ArrayList<Vertice> filhos) {
        this.filhos = filhos;
    }

    public boolean addFilho(Vertice filho) {
        if (this.filhos.contains(filho)) {
            //System.out.println("Filho já existente");
            return false;
        } else {
            this.filhos.add(filho);
            return true;
        }
    }

    public boolean verificaAncestral(Vertice l) {
        Vertice aux = l.getPai();
        while (aux.getEstado() != null) {
            if (aux.getEstado() == l.getEstado()) {
                return false;
            }
            aux = aux.getPai();
        }
        return true;
    }

    public boolean verificaFilho(Vertice filho) {
        return this.filhos.contains(filho); //True se Filho já existe
    }
}
