#include <stdio.h>
#include <string.h>

/* Operadores logicos
  == igua a
  <  menor
  <= menor ou igual
  >  maior
  >= maior ou igual




*/

// exemplo de Codicionais Em C
// fazer uma codicinal que mostre mior e menor de idade de 18 anos

int main()
{

    int idade;           // define a variavel idade
    scanf("%d", &idade); // ler idade da pessoa

    // Analiza se é menor de idade ou nao
    // se
    if (idade < 17)
    {
        printf("Sim é maior de idade");
    }
    // se nao
    else if (idade == 18)
    {
        printf("ja è maior De idade ");
    }

    else if (idade == 19)
    {
        printf("ja è maior De idade com 19 anos  ");
    }
    else
    {
        printf("Atenção é menor de idade");
    }

    return 0;
}
