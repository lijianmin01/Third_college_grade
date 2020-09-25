#include<stdio.h>

int main(){
    char strs[100];
    int cnt=0;
    char c;
    while(scanf("%c",&c)!=EOF){
        if(c=='z'){
            strs[cnt++]='a';
        }else if(c=='Z'){
            strs[cnt++]='A';
        }else{
            strs[cnt++]=(c+1);
        }
    }
    int i;
    for ( i = 0; i < cnt; i++)
    {
        printf("%c ",strs[i]);
    }
    printf("\n");
    
    return 0;
}