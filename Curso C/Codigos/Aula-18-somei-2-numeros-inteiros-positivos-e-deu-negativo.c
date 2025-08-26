#include <stdio.h>


/*
      Aula 18
      tamanho de um int na memória
      intervalo: -2.147.483.648 a 2.147.483.648
      Aula 19
      operador long para o tipo int
      %li / %ld
*/

int main(void) {

  short float x = 3.1415;
  printf("Um float precisa de %d bytes de memória.\n", sizeof x);
  return 0;
}