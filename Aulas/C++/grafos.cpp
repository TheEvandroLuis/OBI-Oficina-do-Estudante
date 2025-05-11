#include<iostream>
#include<vector>
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
};

int main(){
    Grafo grafo(4);
    grafo.addCaminho(1,2);
    grafo.addCaminho(1,3);
    grafo.addCaminho(2,3);
    grafo.addCaminho(3,4);
    grafo.print();
}