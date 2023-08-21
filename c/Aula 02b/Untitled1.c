#include<stdio.h>


void main()
{

    // Saída Padrão
    printf("Hello World \n");

    // Se eu quiser mostrar valores de operações
    // %d para valores inteiros
    // printf("%d", valor);

    // é combinado em ordem.
    printf("%d, com %d, resulta em %d", 5, 3, 5+3);

    // Para valores reais, usamos %f

    // Para limitar as casas decimais, usamos .valor
    // entre % e f (%.2f) - limita a duas casas decimais
    printf("%f, com %f, resulta em %.2f", 5, 3, 5+3);


    /*
    A ordem de operação é PEMDAS
    ou da esquerda para a direita
    */


    return 0;
}
