#include<stdio.h>
int main(){
    int num1[20];
    int num2[20];
    int cnt=0,cnt1;
    int i,j;
    for (int i = 0; i < 20; i++)
    {

        scanf("%d",&cnt1);
        num1[i]=cnt1;
    }

    for(i=1;i<20;i++){
        for(j=0;j<i;j++){
            if((num1[i]/num1[j])==0){
                num2[cnt]=num1[i];
                cnt++;
                break;
            }
        }
    }
    
    for ( i = 0; i < cnt; i++)
    {
        printf("%d\n",num2[cnt]);
    }
    
    return 0;
}