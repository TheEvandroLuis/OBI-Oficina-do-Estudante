#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    int inf, r;
    int total = 0;

    cin >> n >> m;
    cin >> inf >> r;

    vector<int> infectados(n+1, 0);

    //ELIMINA AS REUNIOES COM NENHUM INFECTADO
    for (int i=0; i<r-1; i++ ){
        int presentes;
        cin >> presentes;
        for (int j=0; j<presentes; j++){
            int amigo;
            cin >> amigo;
        }
    }
    //MARCA O PRIMEIRO AMIGO QUE FOI INFECTADO
    infectados[inf] = 1;

    for (int i=r; i<=m; i++){
        int presentes;
        bool reuniao_infectada = false;
        cin >> presentes;
        vector<int> reuniao;

        for (int j=0; j<presentes;j++){
            int amigo;
            cin >> amigo;
            reuniao.push_back(amigo);
            if (infectados[amigo]==1){
                reuniao_infectada=true;
            }
        }
        if(reuniao_infectada){
            for (int pessoa : reuniao){ //for pessoa in reuniao:
                infectados[pessoa]=1;
            }
        }
    }

    for (int infectado:infectados){
        if (infectado){
            total++;
        }
    }

    cout << total << endl;
}