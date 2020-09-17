#include<stdio.h>

int sum(long long int n){
    int i;
    long long int sum1=1;
    for(i=1;i<=n;i++){
        sum1*=i;
    }
    return sum1;
}

int main() {
    long long int n,i;
    long long int sum1=1;
    scanf("%d",&n);
    for ( i = 1; i <=n; i++)
    {
        //printf("%d ",sum1);
        sum1+=sum(i);
    }
    printf("%lld\n",(sum1-1));
    return 0;
}
