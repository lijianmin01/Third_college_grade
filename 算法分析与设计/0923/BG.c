#include<stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    long long int sum=0;
    long long int cnt,temp=1;
    int i;

    for ( i = 1; i <= n; i++)
    {
        temp*=i;
        sum+=temp;
    }
    printf("%lld\n",sum);
    return 0;
}


