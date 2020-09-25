#include<stdio.h>

void jq(int *nums,int n){
    int index,cnt;
    while (n)
    {
        index = n%10;
        n/=10;
        nums[index]++;
    }
    
}

int main(){
    int nums[10];
    int i;
    for ( i = 0; i < 10; i++)
    {
        nums[i]=0;
    }
    int n;
    scanf("%d",&n);
    for ( i = 0; i <=n; i++)
    {
        jq(&nums,i);
    }

    for ( i = 0; i < 10; i++)
    {
        printf("%d\n",nums[i]);
    }
    return 0;
}