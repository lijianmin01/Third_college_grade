#include<stdio.h>

int main(){
    int n;
    int nums[1100];
    int counts,i,j;
    scanf("%d",&n);
    while (n--)
    {
        scanf("%d",&counts);
        for ( i = 0; i < counts; i++)
        {
            scanf("%d",&nums[i]);
        }
        for ( i = 0; i < counts-1; i++)
        {
            for ( j = 0; j < counts-1-i; j++)
            {
                if(nums[j]>nums[j+1]){
                    int cnt=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=cnt;
                }
            } 
        }
        printf("%d\n",nums[(counts+1)/2-1]);
        
    }
    
    return 0;
}