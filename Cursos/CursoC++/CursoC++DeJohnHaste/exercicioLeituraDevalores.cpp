//
// Bibiliotecas Padrao Do C
#include <stdio.h>
#include <stdlib.h>

// ler dois numeors quebrados que imprima os valores em tela
int main()
{

    printf("Digite o valor De A");
    float variavel1;

    printf("   Digite o valor De B");
    float variavel2;

    scanf("%f", &variavel1);
    scanf("%f", &variavel2);
    float resultado = variavel1 + variavel2;

    scanf("%f", &resultado);

    printf("resultado De variavel1 e variavel1 é :%2f", &resultado);

    return 0;
}
