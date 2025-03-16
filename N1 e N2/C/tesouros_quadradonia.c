#include <stdio.h>

int main(void) {
  int m;
  scanf("%d", &m);
  char mapa[m][m];

  int tempo =0;
  int afogado =0;
  int loop=0;
  int continua =1;

  int visitado[m][m];
  //zera a matrix visitado
  for (int i = 0; i < m; i++){
    for(int j = 0; j < m; j++){
      visitado[i][j] = 0;
    }
  }

  //le o mapa
  for (int i = 0; i < m; i++){
    for(int j = 0; j < m; j++){
      scanf(" %c", &mapa[i][j]);
    }
  }
//FORMA MAIS FACIL DE LER A MATRIZ
//for (int i = 0; i < m; i++) scanf("%s", &mapa[i][0]);

  //le a posicao inicial
  int a, b, i, j;
  scanf("%d %d", &a, &b);
  i = a-1;
  j = b-1;

  while(continua){
    if(visitado[i][j]==1){
      loop = 1;
      continua = 0;
    }else{
      //marca como visitado
      visitado[i][j] = 1;

      //navega pelo mapa
      switch (mapa[i][j]){
        case 'N':
          if (i==0){
            continua = 0;
            afogado = 1;
          }else{
            i--;
            tempo++;
          }
        break;
        case 'S':
          if (i==m-1){
            continua = 0;
            afogado = 1;
          }else{
            i++;
            tempo++;
          }
        break;
        case 'O':
          if (j==0){
            continua = 0;
            afogado = 1;
          }else{
            j--;
            tempo++;
          }
        break;
        case 'L':
          if (j==m-1){
            continua = 0;
            afogado = 1;
          }else{
            j++;
            tempo++;
          }
        break;
        case 'X':
          continua = 0;
        break;
      }
    }
  }
  if(afogado) printf("-1");
  else if (loop) printf("0");
  else printf("%d", tempo);

  return 0;
}