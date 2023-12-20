#include <stdio.h>
#include <string.h>

int main()
{

    int num, num2, soma;

    scanf("%d", &num);  // Ler o valor 1
    scanf("%d", &num2); // Ler o valor 2

    soma = num + num2;

    // comparações de valores
    if (soma >= 10)
    {
        printf("sim  maior que  10 ");
    }
    else
    {
        printf("sim é menor que  10 ");
    }
    return 0;
}