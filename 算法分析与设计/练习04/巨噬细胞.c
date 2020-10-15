#include<stdio.h>

int main(){
    char strs[110];
    gets(strs);
    int i;
    for ( i = 0; strs[i]!='\0'; i++)
    {
        if(strs[i]=='9'){
            printf("0");
        }else{
            printf("%c",strs[i]+1);
        }
    }
    printf("\n");
    
    return 0;
}