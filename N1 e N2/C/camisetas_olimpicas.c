#include <stdio.h>

int main(void) {
  int n, p, m;
  int qtdP = 0;
  int qtdM = 0;
  scanf("%d", &n);

  for (int i=0; i<n; i++){
    int op;
    scanf("%d", &op);
    if (op == 1) qtdP++;
    else if (op == 2) qtdM++;
  }
  scanf("%d", &p);
  scanf("%d", &m);
  
  if(qtdP>=p && qtdM>=m) printf("S");
  else printf("N");
  
  return 0;
}