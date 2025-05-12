#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

class Grafo{
    public:
        int n;
        vector<vector<int>> adj;

        Grafo(int vertices){
            n = vertices;
            adj.resize(n+1);
        }

        void addCaminho(int o, int d){
            adj[o].push_back(d);
            adj[d].push_back(o);
        }

        void print(){
            for (int i=1; i<n+1; i++){
                cout << "Vizinhos de " << i << ": ";
                for(int vizinho : adj[i]){
                    cout<< vizinho << " | ";
                }
                cout<<endl;
            }
        }

        vector<int> bfs(int origem, int destino){
            queue<int> fila;
            vector<int> caminho;
            vector<int> pais (n, NULL);
            vector<bool> visitado (n, false);

            pais[origem] = -1;
            fila.push(origem);
            visitado[origem]= true;

            while (!fila.empty()){
                int atual = fila.front();
                fila.pop();
                if (atual==destino){
                    while (atual!=-1){
                        caminho.push_back(atual);
                        atual=pais[atual];  
                    }
                    reverse(caminho.begin(), caminho.end());
                    break;
                }
                
                for (int vizinho:adj[atual]){
                    if (!visitado[vizinho]){
                        visitado[vizinho]=true;
                        pais[vizinho]=atual;
                        fila.push(vizinho);
                    }
                }


            }
            return caminho;
        }
};

int main(){
    Grafo grafo(5);
    grafo.addCaminho(0,3);
    grafo.addCaminho(1,2);
    grafo.addCaminho(1,3);
    grafo.addCaminho(2,3);
    grafo.addCaminho(3,4);
    grafo.print();
    vector<int> caminho = grafo.bfs(1,4);

    for(int no:caminho){
        cout << no << " -> ";
    }
    cout<<endl;
}