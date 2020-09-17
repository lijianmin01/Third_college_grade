#include<stdio.h>

int main(){
    int n,cnt=2,sum=0;
    scanf("%d",&n);
    while (n--)
    {
        sum+=cnt;
        cnt=cnt*10+2;
    }
    printf("%d\n",sum);
    return 0;
}