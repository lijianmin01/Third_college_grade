#include<stdio.h>

int main(){
    int flag,i,result;
    int num;
    scanf("%d",&flag);
    while(flag--){
        result=0;
        for(i=0;i<flag;i++){
            scanf("%d",&num);
            result+=num;
        }
        printf("%d\n",result);
    }
    return 0;
}