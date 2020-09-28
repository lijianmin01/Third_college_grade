#include<stdio.h>

int main(){
    int n;
    long long sum=1;
    long long cnt;
    scanf("%d",&n);
    while (n--)
    {
        scanf("%lld",&cnt);
        sum*=cnt;
    }
    printf("%lld\n",sum);
    
    return 0;
}