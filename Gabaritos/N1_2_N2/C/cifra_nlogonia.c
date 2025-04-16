#include <stdio.h>

int ehVogal(char c);

int main(void) {
  char alfabeto[] = "abcdefghijklmnopqrstuvxz";
  char palavra[30];
  char cifra[100];

  int consoante_index;
  int cifra_index;

  scanf("%s", palavra);

  cifra_index = 0;
  for (int i = 0; palavra[i] != '\0'; i++) {
    //COPIA A PROPRIA LETRA INDEPENDENTE SE VOGAL OU CONSOANTE
    cifra[cifra_index] = palavra[i];
    //SE CONSOANTE
    if(!ehVogal(palavra[i])){
      cifra_index++;
      //ADICIONA A VOGAL MAIS PERTO
      if(palavra[i] < 'd'){
        cifra[cifra_index] = 'a';
      } else if(palavra[i] < 'h'){
        cifra[cifra_index] = 'e';
      } else if(palavra[i] < 'm'){
        cifra[cifra_index] = 'i';
      } else if(palavra[i] < 's'){
        cifra[cifra_index] = 'o';
      } else{
        cifra[cifra_index] = 'u';
      }
      //ADICIONA A PROXIMA CONSOANTE SE NÃO Z
      cifra_index++;
      if(palavra[i]=='z'){
        cifra[cifra_index] = 'z';
      }else{
        consoante_index = strchr(alfabeto, palavra[i]) - alfabeto;
        if(!ehVogal(alfabeto[consoante_index+1])){
          cifra[cifra_index] = alfabeto[consoante_index+1];
        }else{
          cifra[cifra_index] = alfabeto[consoante_index+2];
        }
      }
    }
    cifra_index++;
  }

  printf("%s\n", cifra);

  return 0;
}

int ehVogal(char c) {
  char vogais[] = "aeiou";
  for (int i = 0; vogais[i] != '\0'; i++) {
    if (c == vogais[i]) {
      return 1;
    }
  }
  return 0;
}