#include <stdio.h>
int main(){

float lista1[7], lista2[7];
int i; 
char mes[20];
char *lista[7] = {
    "Domingo",
    "Segunda-Feira",
    "Terca-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sabado",
};
printf("Ola usuario, em qual mes voce esta fazendo essa pesquisa?\n");
scanf("%s", mes);
printf("Usuario, digite as temperaturas da primeira semana, nos respectivos dias do mes de %s:\n ",mes); 
for(i = 0; i < 7; i++){
    printf("%s:\n ", lista[i]);
    scanf("%f", lista1);
}
printf("Certo usuario, agora digite as temperaturas da segunda semana, nos respectivos dias do mes de %s:\n", mes);
for(i = 0; i < 7; i++){
    printf("%s:\n ", lista[i]);
    scanf("%f", lista2);
}
}