#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef struct p{
    int x,y;
    bool operator<(const p &p){
        if(x!=p.x) return x < p.x;
        else return y < p.y;
    }
} ponto;

int main() {
    vector<ponto> pontos;

    ponto novo;
    novo.x=2;
    novo.y=9;
    pontos.push_back(novo);
    novo.x=2;
    novo.y=3;
    pontos.push_back(novo);
    novo.x=2;
    novo.y=1;
    pontos.push_back(novo);

    for(ponto po:pontos){
        cout<< "X: " << po.x << " Y: " << po.y<<endl;
    }
    cout<< "-------------------"<<endl;
    sort(pontos.begin(), pontos.end());


    for(ponto po:pontos){
        cout<< "X: " << po.x << " Y: " << po.y<<endl;
    }

}