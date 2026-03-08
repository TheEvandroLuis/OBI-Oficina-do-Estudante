#include <stdio.h>

int main(void) {
  int n, m, maisVelho;
  scanf("%d", &n);
  scanf("%d", &m);
  maisVelho = m+(m-n);
  printf("%d", maisVelho);
  return 0;
}