#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    vector<int> amigos (101, 0);
    vector<int> tempoRespostaTotal(101, 0);
    int tempo = 0;

    cin >> n;

    for (int i=0; i<n; i++){
        char evento, evento_anterior;
        int valor;
        cin >> evento >> valor;

        //ATUALIZA O TEMPO
        if(evento == 'T'){
            tempo += valor;
        }else{
            if (evento_anterior!='T'){
                tempo++;
            }
        }
        //MARCA QUANDO O AMIGO MANDOU UMA MENSAGEM E QUANDO ELA RESPONDE MARCA O TEMPO TOTAL E ZERA O TEMPO DO AMIGO
        if (evento == 'R'){
            amigos[valor] = tempo;
        }else if ( evento == 'E'){
            tempoRespostaTotal[valor] += (tempo - amigos[valor]);
            amigos [valor] = 0;
        }
        evento_anterior = evento;
    }
    for (int i=1; i<=100; i++){
        if (amigos[i] != 0){
            tempoRespostaTotal[i]=-1;
        }
        if (tempoRespostaTotal[i] != 0){
            cout << i << " " << tempoRespostaTotal[i] << endl;
        }
    }

}