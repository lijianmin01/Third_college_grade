#include<stdio.h>
int panduan(long long int n){
    long long int count = 0;
    while (n)
    {
        if(n%10==6){
            count++;
        }
        n/=10;
    }
    if(count==2){
        return 1;
    }else{
        return 0;
    }

}

int main(){
    long long int n;
    scanf("%d",&n);
    long long int num=0;
    long long int i; 
    if(n<66){
        printf("0\n");
        return 0;
    }
    for ( i = 66; i <= n; i++)
    {
        if(panduan(i)){
            num++;
        }
    }
    printf("%d",num);
    
    return 0;
}