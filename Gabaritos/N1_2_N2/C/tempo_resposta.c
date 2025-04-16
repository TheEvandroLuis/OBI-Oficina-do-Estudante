#include <stdio.h>

//Estou fazendo sem alocação dinamica de memoria porque são poucos dados então não vale a pena
#define MAX_AMIGOS 101

int main(void) {
  //vetor para registrar o momento (tempo_atual) em que um amigo n enviou uma mensagem
  int amigos[MAX_AMIGOS]={0};
  
  //Apos ela responder calcula o tempo de resposta e armazena aqui 
  int tempo_resposta[MAX_AMIGOS]={0};
  
  int n_registros = 0;
  int tempo_atual = 0;
  scanf("%d", &n_registros);
  char comando, comando_anterior;
  int valor;
  
  for (int i = 0; i < n_registros; i++){
    
    scanf("\n%c %d", &comando, &valor);

    //verifico se o comando é T para somar o tempo passado sem atividade, caso contrario soma 1. Observe que se o comando anterior for T, o tempo atual não é somado pq ja foi atualizado
    if(comando == 'T'){
      tempo_atual+=valor;
    }else{
      if(comando_anterior!='T')tempo_atual++;
    }
    if (comando == 'R'){
      amigos[valor] = tempo_atual;
    }
    else if (comando == 'E'){
      tempo_resposta[valor] += tempo_atual - amigos[valor];
      //salva o tempo do amigo com 0 para mostrar que não tem nenhuma mensagem pendente
      amigos[valor] = 0;
    }
    comando_anterior = comando;
    
  }

  for (int i = 1; i < MAX_AMIGOS; i++){
    //caso ela não tenha respondido alguém marca o tempo de espera desse amigo como -1
    if (amigos[i] != 0){
      tempo_resposta[i] = -1;
    }
    if(tempo_resposta[i]!=0){
      printf("%d %d\n", i, tempo_resposta[i]);
    }
  }
  return 0;
}