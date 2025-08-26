#include <stdio.h>

/*
      Aula 17
  Operador short para o tipo int
  intervalo: -32.768 ate 32.767 pode ser utilizado o short int
  %hi ou %d

*/
int main(void) {

  short int x = 32767;

  printf("Tamanho de um float na memoria: %d bytes\n", sizeof x);

  printf("Hello World\n");
  return 0;
}