#include<stdio.h>

int main() {
    int nums[4],i,j;
    for ( i = 0; i < 4; i++)
    {
        scanf("%d",&nums[i]);
    }
    for ( i = 0; i < 3; i++)
    {
        for ( j = 0; j < 3-i; j++)
        {
            if(nums[j]>nums[j+1]){
                int cnt=nums[j+1];
                nums[j+1]=nums[j];
                nums[j]=cnt;
            }
        }
    }
    for ( i = 0; i < 4; i++)
    {
        printf("%d ",nums[i]);
    }
    
    return 0;
}
