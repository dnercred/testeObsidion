//
#include <stdio.h>
#include <string.h>

/*
 Fazer um progrma que informe se ele é par ou impa


*/

int main()
{

    int num;
    // ler Valores
    scanf("%d", &num);

    // O operador % tras como resultado
    // o Resto Da Divisao de um numero por outro Numero
    if (num % 2 == 0)
    {
        printf("sim é um numero par");
    }

    else
    {
        printf("Atençao nao é um numero par ");
    }
    return 0;
}