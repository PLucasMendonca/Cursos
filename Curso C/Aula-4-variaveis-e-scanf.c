#include <stdio.h>
#include <stdlib.h>

/*
      Aula 4
  Lendo números inteiros
*/
int main(void) {

  int valor, valor2; // Criei uma variavel para guardar um valor do tipo inteiro

  //Atribuição -> atribuir um valor a uma variável
  valor = 50;
  printf("Digite um valor inteiro: ");
  scanf("%d", &valor);
  printf("Digite um segundo valor inteiro: ");
  scanf("%d", &valor2);
    printf("\n\nPrimeiro valor: %d\nSegundo valor: %d", valor, valor2);
  return 0;
}