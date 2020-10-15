#include<stdio.h>

void func(int num){
    int nums[999999];
    int count=0;//记录因数个数
    int sum = 0;//记录因数的和
    int i,j;
    for ( i = 1; i <= num/2; i++)
    {
        if(num%i==0){
            nums[count++]=i;
            sum+=i;
        }
    }
    if(sum==num){
        printf("%d:");
    }
    for ( i = 0; i < count; i++)
    {
        printf("%d ",nums[i]);
    }
    printf("\n");

}

int main(){
    int i;
    for ( i = 6; i < 10001; i++)
    {
        func(i);
    }
    
    return 0;
}