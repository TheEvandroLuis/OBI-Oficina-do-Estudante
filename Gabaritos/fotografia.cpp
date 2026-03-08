#include <iostream>
using namespace std;

typedef struct {
    int altura;
    int largura;
    int id;
}Moldura;

int encaixa (Moldura moldura, int a, int l); //responde se a foto de medidas a e l cabe na moldura vira ou regular
int menorque(Moldura moldura1, Moldura moldura2); //responde se moldura1 eh menor que moldura 2

int main(){
    int a, l;
    int n;
    Moldura melhor;

    melhor.altura = 201;
    melhor.largura =201;
    melhor.id = -1;

    cin >> a >> l;
    cin >> n;

    for (int i=0; i<n; i++){
        Moldura moldura;
        cin >> moldura.altura >> moldura.largura;
        moldura.id = i+1;

        if (encaixa(moldura, a, l) && menorque(moldura, melhor)){
            melhor.altura= moldura.altura;
            melhor.largura= moldura.largura;
            melhor.id= moldura.id;
        }
    }
    cout<< melhor.id << endl;
}

int encaixa (Moldura moldura, int a, int l){
    //cout<< "MOLDURA: " << moldura.altura << " | " << moldura.largura << " a: " << a << " l: " <<l<<endl;
    if ((moldura.altura>=a && moldura.largura>=l) || (moldura.altura>=l && moldura.largura>=a)){
        //cout<<"Foto cabe" << endl;
        return 1;
    }
    //cout<<"foto não cabe" << endl;
    return 0;
}

int menorque(Moldura moldura1, Moldura moldura2){
    if ((moldura1.altura*moldura1.largura) < (moldura2.altura*moldura2.largura)){
        //cout<<"Menor que a melhor" << endl;
        return 1;
    }
    //cout<<"Melhor é menor" << endl;
    return 0;
}