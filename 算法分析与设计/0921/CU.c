#include<stdio.h>

int main(){
    char st1[3],st2[3],st3[3];
    int i,j;
    gets(st1);
    gets(st2);
    gets(st3);
    

    for ( i = 0; i < 3; i++)
    {
        printf("%c %c %c\n",st1[i],st2[i],st3[i]);
    }
    
    return 0;
}