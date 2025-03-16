#include <stdio.h>
#include <string.h>

#define TAMANHOMAX 100001

typedef struct pilha{
    int topo;
    char pilha[TAMANHOMAX];
}Pilha;

int bemDefinida(char *entrada){
  Pilha pilha;
  pilha.topo =-1;

  for (int i=0; i<strlen(entrada); i++){
    if (entrada[i] == '(' || entrada[i] == '[' || entrada[i] == '{'){
      pilha.pilha[++pilha.topo] = entrada[i];
    }else{
      if(pilha.topo == -1){
        return 0;
      }else{
        if (entrada[i] == ')' && pilha.pilha[pilha.topo]== '(' ||
            entrada[i] == ']' && pilha.pilha[pilha.topo]== '[' ||
            entrada[i] == '}' && pilha.pilha[pilha.topo]== '{'){
          pilha.topo--;
        }
        else return 0;
      }
    }
  }
  if (pilha.topo == -1) return 1;
  else return 0;
}

int main(void) {
  int n;
  scanf("%d", &n);

  for(int i=0; i<n; i++){
    char entrada[TAMANHOMAX];
    scanf("%s", entrada);

    if(bemDefinida(entrada)) printf("S\n");
    else printf("N\n");    
  }  
  return 0;
}