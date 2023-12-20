#include <stdio.h>
#include <string.h>

/*Fazerum progrma que leia dois numeros interios
    e imprima na tela o Qual o maior
    Entre eles ou se sao Iguais
*/

int mai()
{

    int num, num2;
    // ler Valores
    scanf("%d", &num);
    scanf("%d", &num2);

    // Comparaçoes

    if (num > num2)
    {
        printf("no numero 1 é maior o que numero 2");
    }
    else if (num < num2)
    {
        printf("no numero 1 é maior o que numero 2");
    }
    else
    {
        printf("no numero 1 é igual o que numero 2");
    }

    return 0;
}