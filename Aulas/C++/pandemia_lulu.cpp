#include <iostream>
#include <vector>
using namespace std;

void imprimirMatriz(const std::vector<std::vector<int>>& matriz) {
    // Usamos range-based for loops com 'const auto&' para performance e segurança
    for (const auto& linha : matriz) {
        for (int valor : linha) {
            std::cout << valor << " ";
        }
        std::cout << '\n'; // Preferimos '\n' no lugar de std::endl
    }
}

void imprimirVetor(const std::vector<int>& vetor) {
    // Range-based for loop: limpo, direto e seguro
    for (int valor : vetor) {
        std::cout << valor << " ";
    }
    std::cout << '\n';
}

int main(){
    int amg, reu, amg_inf, reu_inf, participantes;
    cin>>amg>>reu;
    cin>>amg_inf>>reu_inf;
    vector<int> condicao(amg+1,0);
    vector<vector<int>> reuniao;

    for(int i=1; i<=reu; i++){
        cin>>participantes;
        vector<int> amg_p(amg,0);
        for(int j=0; j<participantes; j++){         
            int b;
            cin>>b;
            amg_p[j]=b;
        }
        reuniao.push_back(amg_p);
    }

    for(int i=0; i<reu; i++){
        for( int j=0; j<amg; j++){
            if (i==reu_inf-1){
                int p;
                p=reuniao[i][j];
                condicao[p]=1;
            }  
            else if(i>reu_inf-1){
                int c;
                c=reuniao[i][j];
                if(condicao[c]==1){
                    int q;
                    q= reuniao[i].size();
                    for( int w=0; w<q; w++){
                        int l;
                        l=reuniao[i][w];
                        condicao[l]=1;
                    }
                }    
            }
        }   
        //imprimirVetor(condicao); 
    } 
    
    int contaminados;
    contaminados=0;
    int d;
    d=condicao.size();
    for(int a=1; a<=d; a++){
        if(condicao[a]==1){
            contaminados++;
        }
    }
    cout<<contaminados;
}