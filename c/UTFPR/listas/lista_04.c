/*
===================================================
1
Recebe 3 numeros distindos e os mostra em ordem crescente.

Deve usar apenas 3 variaveis, e seus conteudos nao devem ser modificados apos a
leitura
===================================================
*/
/*
#include<stdio.h>

int main()
{

  int val1, val2, val3;

  // Entrada de dados
  printf("Digite o primeiro valor");
  scanf("%d", &val1);

  printf("Digite o segundo valor");
  scanf("%d",&val2);

  printf("Digite o terceiro valor");
  scanf("%d",&val3);


  if(val1>val2) // Val1 > Val2
  {
    if(val2>val3)
      printf("A ordem é %d, %d, %d", val1, val2, val3);

    else
      printf("A ordem é %d, %d, %d", val1, val3, val2);

  }
  else if(val2>val1){
    if(val1>val3)
      printf("A ordem é %d, %d, %d", val2, val1, val3);

    else
      printf("A ordem é %d, %d, %d", val1, val3, val2);

  }
  else{
    if(val2>val1)
      printf("A ordem é %d, %d, %d", val3, val2, val1);

      else
        printf("A ordem é %d, %d, %d", val3, val1, val2);

  }

  return 0;
}
 // Conferir dps

*/
/*
=============================================================
2. Escreva um programa que recebe a data de nascimento de uma pessoa e a data
atual (no formato dd/mm/aaaa), calcule e apresente a idade da pessoa.

===========================================================
 JÁ FIZ *************************8

 ============================================================

==============================================================
3. A organização da OIBR, Olimpíada Internacional de Basquete de Robô, está
começando a ter problemas com dois times: os Bit Warriors e os Byte Bulls. É que
os robôs desses times acertam quase todos os lançamentos, de qualquer posição na
quadra! Pensando bem, o jogo de basquete ficaria mesmo sem graça se jogadores
conseguissem acertar qualquer lançamento, não é mesmo? Uma das medidas que a
OIBR está implantando é uma nova pontuação para os lançamentos, de acordo com a
distância do robô para o início da quadra. A quadra tem 2000 centímetros de
comprimento, como na figura.

Dada a distância D, em cm, do robô até o início da quadra, onde está a cesta, a
regra é a seguinte: • Se D ≤ 800, a cesta vale 1 ponto; • Se 800 < D ≤ 1400, a
cesta vale 2 pontos; • Se 1400 < D ≤ 2000, a cesta vale 3 pontos.

A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o
valor da distância D, você deve escrever um programa para calcular o número de
pontos do lançamento: 1, 2 ou 3.
==============================================================

*/

/*
#include <stdio.h>

int main() {

  int dist = 2000, robot_dist;

  // Entrada de dados
  printf("Digite a distância: \n");
  scanf("%d", &robot_dist);

  if ((robot_dist < 2000) && robot_dist > 800 &&
      (robot_dist < 1400 || robot_dist = 1400)) { // 2 pt
    printf("A cesta vale 2 pontos. \n");
  } else if ((robot_dist < 2000) && (robot_dist < 800 || robot_dist <= 800) &&
             robot_dist > 0) { // 1 pt
    printf("A cesta vale 1 pontos.\n");
  } else if ((robot_dist < 2000) && (robot_dist > 1400)) { // 3 pt
    printf("A cesta vale 3 pontos.\n");
  }

  return 0;


  ****************** OTIMIZAR DEPOIS ****************************
  - if lógico final <800
  - sem printf
}
*/

/*
==============================================================
4. Suponha que você está programando um módulo contador de cédulas para caixas
eletrônicos. Escreva um programa que informa com quantas cédulas de Real podemos
representar um dado valor, considerando que existem cédulas de 1, 2, 5, 10, 20,
50 e 100 Reais. Exemplo de resposta: R$ 218 = 2 cédulas de 100, 1 cédula de 10,
1 cédula de 5, 1 cédula de 2 e 1 cédula de 1. O número de cédulas usadas deve
ser o menor possível. Desconsidere valores com centavos, e suponha que a máquina
sempre tem disponíveis as cédulas necessárias.
==============================================================
*/

/*
#include <stdio.h>

int main() {

  int valor, ced_cent, ced_dez, ced_uni,
      qtd_cent, qtd_dez, qtd_uni;

  // Entrada de dados
  printf("Digite o valor em real: \n");
  scanf("%d", &valor);

 // 925

  ced_cent = valor / 100; //9
  ced_dez = valor % 100; // 25
  ced_uni = valor % 10; // 5

  printf("Cent %d, Dez %d, Un %d\n", ced_cent, ced_dez, ced_uni);

  // Quantidade de Cédulas
  //printf("Precisará %d de 100R$, %d de 10R$ e %d de 1R$: \n", ced_cent,
ced_dez, ced_uni);

  if(ced_uni%2==1){ // Impar
    if(ced_uni>=5){ // Unidade > 5
      printf("Unidade > 5 Impar\n");
      printf("Precisará %d de 100R$, %d de 10R$, 1 de 5R$ e %d de 1R$: \n",
ced_cent, ced_dez, ced_uni-5);
    }
    else{ // Unidade < 5
      printf("Unidade < 5 Impar\n");
      printf("Precisará %d de 100R$, %d de 10R$ e %d de 1R$: \n", ced_cent,
ced_dez, 5-ced_uni);
    }
      printf("Precisará %d de 100R$, %d de 10R$ e %d de 1R$: \n", ced_cent,
ced_dez, ced_uni);
  }
  else{ // Par
    if(ced_uni>5){ // Unidade > 5
      printf("Unidade > 5 Par\n");
      printf("Precisará %d de 100R$, %d de 10R$, 1 de 5R$ e %d de 2R$: \n",
ced_cent, ced_dez, ced_uni/2);
    }
    else{ // Unidade < 5
      printf("Unidade < 5 Par\n");
      printf("Precisará %d de 100R$, %d de 10R$ e %d de 2R$: \n", ced_cent,
ced_dez, ced_uni/2);
    }

  }

  return 0;
}


*/
/*
======================================
5. Escreva um programa que recebe 3 valores e verifica se eles podem ser os
comprimentos dos lados de um triângulo. Em caso positivo, escrever uma mensagem
informando se é um triângulo isósceles, equilátero ou escaleno. Obs.: o
comprimento de um lado do triângulo é sempre menor do que a soma dos outros
dois.

Isósceles cat1 = cat ||
Equilátero cat1=cat2=cat3
Escaleno cat1 != cat2 != cat3
=======================================
*/

/*
#include<stdio.h>

int main(){

  int cat1, cat2, cat3; // cateto

  // Entrada de dados
  printf("Digite o primeiro cateto: \n");
  scanf("%d", &cat1);

  printf("Digite o segundo cateto: \n");
  scanf("%d", &cat2);

  printf("Digite o terceiro cateto: \n");
  scanf("%d", &cat3);



  // É um triângulo?

  if(cat1 < (cat2+cat3)){
      if(cat2 < (cat1+cat3)){
        if(cat3 < (cat1+cat2)){
          if(cat1==cat2==cat3){ // Equilátero
            printf("O triângulo é Equilátero");
           }
           else if((cat1 == cat2) || (cat1 == cat3) || (cat2 == cat3)){ //
Isósceles printf("O triângulo é Isósceles");
            }

            else{ // Escaleno
              printf("O triângulo é Escaleno");
           }

        }
      }
    }
    else{
    printf("Não é um triângulo\n");
    }
  return 0;
}

*/
/*
===============================================================================
(****) 6. OPCIONAL! Ainda considerando o seu trabalho com caixas eletrônicos,
você deve escrever um programa que recebe um número de conta-corrente com três
dígitos e mostra o seu dígito verificador. O dígito verificador é calculado da
seguinte forma (utilizando o número 235 como exemplo):
- Some o número da conta com o mesmo número com os dígitos invertidos. Exemplo:
235 + 532 = 767 (o algoritmo para realizar esta inversão já foi visto em outro
exercício).
- Se a soma anterior for maior ou igual a 1000, desconsidere o milhar.
- Separe os 3 dígitos do número resultante, multiplicando a centena por 1, a
dezena por 2, e a unidade por 3. Some os 3 valores. Exemplo: 7 (posição 1), 6
(posição 2) e 7 (posição 3): (7 x 1) + (6 x 2) + (7 x 3) = 7 + 12 + 21 = 40.
- O último dígito desse resultado é o dígito verificador da conta. Exemplo: 0.
===============================================================================
*/

#include <stdio.h>

int main() {

  int conta, dig_ver, uni, dez, cent;

  // Entrada
  printf("Digite a conta (3 dígitos)): \n");
  scanf("%d", &conta);

  // Casas
  cent = conta / 100;
  dez = conta / 10;
  uni = conta % 10;

  // Dígito Verificador (Etapa 1)
  dig_ver = (uni + dez + cent) + conta;
  printf("Etapa 1, O dígito verificador é: %d\n", dig_ver);

  // Maior que 1000
  if (dig_ver >= 1000) {
    dig_ver = 1000 - dig_ver;
    printf("Etapa 1.1, O dígito verificador é: %d\n", dig_ver); // Etapa 1.1
  }

  // Separação
  cent = (dig_ver / 100);
  dez = (dig_ver / 10) * 10;
  uni = (dig_ver % 10) * 3;

  //  Etapa 2
  printf("Etapa 2, Centenas %d, Dezenas %d, Unidades %d\n", cent, dez, uni);

  dig_ver = cent + dez + uni;

  //  Etapa 3
  printf("Etapa 3, O dígito verificador é: %d\n", dig_ver); // Etapa 1.1

  dig_ver = dig_ver % 100;

  printf("O dígito verificador é: %d \n", dig_ver);

  return 0;
}