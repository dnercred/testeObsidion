TIPOS DE VARIAVEIS 


O tipo de dado inteiro: int
Este tipo de dado serve para armazenar, especificamente, dados numéricos do tipo inteiro.
Os inteiros são:
..., -3, -2, -1, 0, 1, 2, 3, ...


Vamos agora criar e declarar uma variável chamada idade:
int idade;


Pronto. Nesse ponto, o computador vai pegar um local da memória do seu computador e reservar para a variável idade. E o que está armazenado? Inicialmente, 'lixo'.

Vamos agora atribuir o valor 18 para esta variável:
idade = 18;


Agora, sempre que usarmos a variável numero, ela será substituída pelo número inteiro 18.
Veja:
#include <iostream>
using namespace std;

int main()
{
    int idade;
    idade = 18;

    cout << "Minha idade é: "<< idade <<endl;
    return 0;
}

Note que o cout não imprime a palavra 'idade', e sim o valor contido dentro desta variável.
Variável em C++


Tipo de dado caractere: char
Além de números inteiros, podemos também armazenar caracteres, ou seja, letras.
Para isso, usamos a palavra-chave char (de character, do inglês).

Vamos declarar uma variável do tipo char, de nome letra.
char letra;

Agora vamos atribuir um valor para ela. No caso, como é um char, devemos armazenar alguma letra do alfabeto, como por exemplo, C:
letra = 'C';


Note que os caracteres devem estar dentro de aspas simples.
Vamos imprimir essa letra na tela:

#include <iostream>
using namespace std;

int main()
{
    char letra;
    letra = 'C';

    cout << "A terceira letra do alfabeto é: "<< letra << endl;
    return 0;
}

Resultado:
Variáveis em C++

Lembrando que 'a' é diferente de 'A', são dois caracteres distintos.
Os caracteres são mais usados em conjuntos, ou seja, formando um texto. Vamos estudar isso em uma seção posterior de nosso curso, sobre strings.

Veja que:
5 - é um número, um dado do tipo int
'5' - é um caractere, uma letra, não pode ser usado por exemplo em operações matemáticas

Tipo de dado flutuante: float e double
Já aprendemos a lidar com números inteiros.
Porém, nem tudo na vida é um número inteiro, como sua idade.

Muitas vezes, precisamos trabalhar com valores fracionados, ou seja, 'quebrados'.
Para isso, usamos os tipos de dados float e double:
float preco;
double valor;

A diferença é que float tem precisão única, e double tem precisão dupla (ou seja, cabe uma parte fracionada maior, e um maior número de bytes da memória foi reservado para este tipo de variável).

Vejamos um uso:

#include <iostream>
using namespace std;

int main()
{
    float preco;
    preco = 14.99;

    cout << "A apostila custa: R$ "<< preco << endl;
    return 0;
}

Note que usamos ponto (.) ao invés de vírgula (,). É assim que usamos em programação, como nos Estados Unidos, por exemplo.
Tipo de dado double

Assim, uma lojinha de R$ 1,99 em nosso mundo, será lojinha de R$ 1.99 no mundo da programação, ok?

O tipo de dado Booleano: bool
Você já deve ter ouvido falar que na computação (ou na tecnologia, de um modo geral), é tudo 1 ou 0, não é?

De fato, os valores 1 e 0, são muito importantes, pois representam verdadeiro e falso, consecutivamente.

Existe um tipo de dado para armazenar somente informações do tipo true/false (chamados de booleanos), o bool.

Declarando:
bool verdade;


Atribuindo um valor booleano:
verdade = true;


Exibindo o valor de true na tela:

#include <iostream>
using namespace std;

int main()
{
    bool verdade;
    verdade = true;

    cout << "Verdade em C++ é: "<< verdade << endl;
    return 0;
}

Resultado:
Curso de C++ completo online grátis para download

Exercícios:
1. Faça um programa em C++ que exibe o valor de duas variáveis, do tipo booleano, mostrando cada valor atribuído possível. Use duas variáveis.

2. Refaça o exercício anterior, agora declarando apenas uma variável.

Nomes de variáveis
Como temos total poder para escolhermos o nome que quisermos para nossas variáveis, temos também algumas responsabilidades.

A primeira delas é não escolher palavras-chaves (keywords), que serão listas no tópico a seguir.
Outra responsabilidade, é a da organização.

Você vai ficar tentado a usar:
int a, float b, char c

Evite esses nomes. Use:
int idade;
float diametro;
char letra;

Ou seja, nomes de variáveis que queiram significar algo relacionado ao valor que você vai armazenar ali. Isso ajuda muito quando seus programas forem se tornando maiores e mais complexos.

Evite também:
double salarioprogramador;

Use:
double salario_programador;

Ou ainda:
double salarioProgramador;

Note como assim fica mais fácil de ler e de cara já podemos antever que tipo de informação tem nessas variáveis, concorda?

Palavras-chave reservadas
Existem algumas palavras que você não deve usar como nomes para suas variáveis, pois elas são reservadas para o funcionamento interno do C++.

São elas:
and, and_eq, asm, auto, bitand, bitor, bool, break, case, catch, char, class, compl, const, canst cast, continue, default, delete, do, double, dynamic_ cast, else, enum, explicit, export, extern, false, float, for, friend, goto, if, inline, int, long, mutable, namespace, new, not, not_ eq, operator, or, or_eq, private, protected, public, reg i ster, reinterpret_cast, return, short, signed, sizeof, static, static_cast, struct, switch, template, this, throw, true, try, typedef, typeid, typename, union, unsigned, us ing, virtual, void, volatile, wchart, while, xorxor_eq

Resposta do exercício
#include <iostream>
using namespace std;

int main()
{
    bool valorBooleano;
    valorBooleano = true;
    cout << "Verdade em C++ é: "<< valorBooleano << endl;

    valorBooleano = false;
    cout << "Falso em C++ é: " << valorBooleano << endl;
    return 0;
}

