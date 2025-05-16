#include <stdio.h>
int main(){

    int i;
    float med, soma;

    char *lista1[7] = {
        "Domingo",
        "Segunda-Feira",
        "Terça-Feira",
        "Quarta-Feira",
        "Quinta-Feira",
        "Sexta-Feira",
        "Sabado"
    };
    float lista2[7] = {
        27,
        30,
        27.6,
        23.5,
        29.3,
        24,
        21
    };
    soma = 0.0;
    for(i = 0; i <7; i++){
        soma += lista2[i];
    }
    med = soma/7;
    for(i = 0; i <7; i++){
        if (lista2[i] < med){
            printf("Os dias da semana, nos quais apresentaram temperaturas abaixo da media foram: %s: %.2f\n", lista1[i], lista2[i]);
        }
    }


    
}