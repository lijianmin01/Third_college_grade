
#include<stdio.h>

int main() {
    int num1[6];
    int num2[8];
    int i,j;
    for ( i = 0; i < 6; i++)
    {
        scanf("%d",&num1[i]);
    }
    for ( i = 0; i < 8; i++)
    {
        scanf("%d",&num2[i]);
    }

    int num3[6];
    int cnt=0;
    for(i=0;i<6;i++){
        for(j=0;j<8;j++){
            if(num1[i]==num2[j]){
                if(cnt==0){
                    num3[cnt++]=num1[i];
                }else{
                    if(num1[i]!=num3[cnt-1]){
                        num3[cnt++]=num1[i];
                    }
                }
                break;
            }
        }
    }
    for ( i = 0; i < cnt; i++)
    {
        printf("%d\n",num3[i]);
    }
    
    
    return 0;
}