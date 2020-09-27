#include<stdio.h>
#include<string.h>

int main(void){
    char str1[100];
    gets(str1);
    int len=strlen(str1),i;
    for ( i = 0; str1[i]!='\0'; i++)
    {
        str1[2*len-1-i]=str1[i];
    }
    str1[2*len]='\0';
    for ( i = 0; i < 2*len; i++)
    {
        printf("%c",str1[i]);
    }
    printf("\n");
    
    return 0;
}