/* 
=====/=====/=====/=====/=====/=====/=====/=====/=====/=====

  foo = 5;
  if(foo++ > 5) // Falso!! Pois o valor será incrementado depois
  if(++foo > 5) // Verdadeiro!!

  if - repete uma única vez se a condição for verdadeira
  while - se repete até a condição for falsa

  Posso ter mais que uma inicialização:

  for(inicialização; condição)
  for(int i=0, b = 0, c = 0; condição)

  Para Condicionais, devemos tomar cuidado que qualquer coisa diferente de 0 é
interpretada como VERDADEIRO.

"if(foo==1)" não é equivalente a "if(foo)"
Se foo tiver qualquer outro valor armazenado, será
dado como True.

Nas combinações relacionais, a ordem é sempre da esquerda 
para a direita!

if(18 <= idade <= 60)

Ou seja, 18 <= idade resultará em 0 ou 1, ficando assim:

if(1<=60) ou
if(0<=60)

Ordem dos Operadores:

1° !
2° * / %
3° + -
4° < > <= >=
5° == !=
6° &&
7° ||

Alguns compiladores já fazem até o seu resultado ser reconhecido

A || ((b>10) && c)

Se A for 1, não precisa verificar o resto, pois já será verdadeiro
independente do resto.


Tomar cuidado com a verificação e legibilidade, pois

EXP1 || (EXP2 && EXP3)

é tranquilo de ler e facilidade a legibilidade geral,
porém redunda pois && será realizado antes de ||

(EXP1 || EXP2) && EXP3

Já aqui é necessário se for o caso de verificar || antes.


Operadores:

foo = 5;
  if(foo++ > 5) // Falso!! Pois o valor será incrementado depois
  if(++foo > 5) // Verdadeiro!!


  #define <NOME> <código>

  // A ideia é que a cada vez que ocorrer aquele NOME, ele substituirá pelo que 
  estiver à direita

1° Loops Determinados (quando conhecemos a quantidade de vezes a serem repetidas)

  2° Loops Indeterminados (quando não conhecemos, mas sabemos o objetivo)

  3° Repetições Aninhadas
  
  * Iteração = Repetição

for(inicialização; condição)

  Mas posso ter mais que uma inicialização:

  for(int i=0, b = 0, c = 0.)
  
=====/=====/=====/=====/=====/=====/=====/=====/=====/=====

#include<stdio.h>

int main(){


  return 0;
}
*/