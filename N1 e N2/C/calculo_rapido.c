#include <stdio.h>

int main(void) {
  int s, a, b;
  int qtdNumeros = 0;
  scanf("%d\n%d\n%d", &s, &a, &b);

  for(int i=a; i<=b; i++){
    int soma =0;
    int numero = i;
    while(numero>=10){
      soma += numero%10;
      numero = numero/10;
    }
    soma +=numero;
    if(soma==s) qtdNumeros++;  
  }

  printf("%d" , qtdNumeros);
  
  return 0;
}