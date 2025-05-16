#include <stdio.h>

int main() {
    float temp[3][7];
    float soma = 0.0, media;
    float menor, maior;
    int i, j;


    for (i = 0; i < 3; i++) {
        printf("Semana %d:\n", i + 1);
        for (j = 0; j < 7; j++) {
            printf("Digite a temperatura do dia %d: ", j + 1);
            scanf("%f", &temp[i][j]);
            soma += temp[i][j];
        }
    }


    menor = temp[0][0];
    maior = temp[0][0];


    for (i = 0; i < 3; i++) {
        for (j = 0; j < 7; j++) {
            if (temp[i][j] < menor) {
                menor = temp[i][j];
            }
            if (temp[i][j] > maior) {
                maior = temp[i][j];
            }
        }
    }

    media = soma / (3 * 7);


    printf("A menor temperatura identificada foi: %.2f\n", menor);
    printf("A maior temperatura identificada foi: %.2f\n", maior);
    printf("Temperaturas abaixo da média (%.2f):\n", media);

    
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 7; j++) {
            if (temp[i][j] < media) {
                printf("Semana %d, Dia %d: %.2f\n", i + 1, j + 1, temp[i][j]);
            }
        }
    }

    return 0;
}
