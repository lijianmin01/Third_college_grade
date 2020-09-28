#include<stdio.h>

int main() {
    int n,a,b,c;
    scanf("%d",&n);
    while(n!=0){
        a = n%10;
        b = n/10%10;
        c = n/100;
        if((a*a*a+b*b*b+c*c*c)==n){
            printf("Yes\n");
        }else{
            printf("No\n");
        }
        scanf("%d",&n);
    }
    return 0;
}