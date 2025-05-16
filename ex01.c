#include <stdio.h>
int main(){

    float maior, menor;
    int i;
    float lista [7];
    lista[0] = 27;
    lista[1] = 30;
    lista[2] = 27.6;
    lista[3] = 23.5;
    lista[4] = 29.3;
    lista[5] = 24;
    lista[6] = 21;
    maior = lista[0];
    menor = lista[0];
    for(i = 1; i < 7; i++){
        if (lista[i] > maior){
            maior = lista[i];
        }
        if (lista[i] < menor){
            menor = lista[i];
        }

    }
    printf("A maior temperatura foi %.2f\n A menor temperatura foi %.2f\n", maior, menor);





}