#include<stdio.h>

int main(){
    int nums[30];
    int i,j;
    int n,cnt;
    nums[1]=1;
    nums[2]=1;
    for ( i = 3; i < 30; i++)
    {
        nums[i]=nums[i-1]+nums[i-2];
    }
    scanf("%d",&n);
    while(n--){
        scanf("%d",&cnt);
        printf("%d\n",nums[cnt]);
    }
    
    return 0;
}