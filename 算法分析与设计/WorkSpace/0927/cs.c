#include<stdio.h>

int main() {
    int n;
    char str[5],cnt;
    int i,j;
    scanf("%d",&n);
    while(n--){
        scanf("%s",str);
        for ( i = 0; i < 2; i++)
        {
            for ( j = 0; j < 2-i; j++)
            {
                if(str[j]>str[j+1]){
                    cnt=str[j];
                    str[j]=str[j+1];
                    str[j+1]=cnt;
                }
            }
            
        }
        for ( i = 0; i < 3; i++)
        {
            printf("%c",str[i]);
            if(i!=2){
                printf(" ");
            }else{
                printf("\n");
            }
        }
        
        
    }
    return 0;
}