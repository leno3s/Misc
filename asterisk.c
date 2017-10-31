#include<stdio.h>
int main(int argc, char *argv[]);

int main(int argc, char *argv[])
{
    int height;
    scanf("%d", &height);

    for(int i = 0; i < height; i++){
        for(int j = 1; height - i; j++){
            printf(" ");
        }
        for(int k = 1; 2 * i - 1 < k; k++){
            printf("*");
        }
        printf("\n");
    }
}
