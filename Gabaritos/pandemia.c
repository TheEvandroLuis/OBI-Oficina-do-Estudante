#include <stdio.h>

int main(void) {
  int n, m;
  int i, r;

  scanf("%d %d", &n, &m);
  scanf("%d %d", &i, &r);

  int infectados[n+1];
  int totalInfectados =0;
  int n_participantes, descarte;
  
  for(int j=0; j<n+1; ++j){
    infectados[j] = 0;  
  }
  infectados[i]=1;
  
  for(int j=1; j<r; j++){
    scanf("%d", &n_participantes);
    for(int k=0; k<n_participantes; k++){
      scanf("%d", &descarte);
    }
  }

  for (int j=r; j<=m; j++){
    scanf("%d", &n_participantes);
    int participantes[n_participantes];
    int rcontaminada =0;
    
    for(int k=0; k<n_participantes; k++){
      scanf("%d", &participantes[k]);
      if(infectados[participantes[k]]==1) rcontaminada=1;
    }
    
    if(rcontaminada){
      for(int k=0; k<n_participantes; k++){
        infectados[participantes[k]]=1;
      }
    }
  }

  for(int j=1; j<n+1; j++){
    if(infectados[j]==1) totalInfectados++;
  }
  
  printf("%d", totalInfectados);

  return 0;
}