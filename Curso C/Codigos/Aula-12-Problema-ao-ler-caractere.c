#include <stdio.h>

/*
        Aula 12
    Ler idade, peso, altura e sexo
*/
int main(void) {
  char sexo;
  int idade;
  float peso, altura;

  printf("Digite sua idade, peso, altura e seu sexo f ou m: ");
  scanf("%d%f%f %c", &idade, &peso, &altura, &sexo);
  printf("Sexo: %c\nIdade: %d\nPeso: %.2f\nAltura: %.2f\n", sexo, idade, peso, altura);
  
  return 0;
}