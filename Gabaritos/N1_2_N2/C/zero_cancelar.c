#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int n=1, soma = 0, topo =0;
  scanf("%d", &n);
  int* valores = malloc(sizeof(int)*n);

  for (int i=0; i<n; i++){
    int entrada;
    scanf("%d", &entrada);
    if(entrada==0 && topo>0){
      topo--;
    }else{
      valores[topo] = entrada;
      topo++;
    }
  }

  for (int i=0; i<topo; i++){
    soma += valores[i];
  }
  printf("%d", soma);
  return 0;
}