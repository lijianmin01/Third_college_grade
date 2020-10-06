#include<stdio.h>

int main(){
    long long int n;
    int arr[100000];
    int len;
    int i;
    while(scanf("%lld",&n)!=EOF){
        if(n==0){
            printf("0\n");
        }else{
            len = 0;
            while(n){
                arr[len++]=n%2;
                n=n/2;
            }
            for ( i = len-1; i >= 0; i--)
            {
                printf("%d",arr[i]);
            }
                printf("\n");
            }
    }
    return 0;
}