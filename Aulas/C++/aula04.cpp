#include <iostream>
#include<string>
#include<vector>
using namespace std;

typedef struct aluno {
    string nome;
    int RA;
    int ano;
    char Turma;
} Aluno;

int main() {
    vector<Aluno> alunos;
    int n;
    cin >> n;

    for (int i=0; i<n; i++){
        Aluno novo;
        cout<< "Nome: ";
        cin >> novo.nome;
        cout << "RA: ";
        cin>> novo.RA;
        alunos.push_back(novo);
    }

    for (Aluno aluno: alunos){
        cout << "Nome: " << aluno.nome << " RA: " << aluno.RA<< endl;
    }
}

