#include<stdio.h>

int main(){
    int n;
    //int nums1[110],nums2[110];
    int nums[220];
    int count,i,j,cnt;
    scanf("%d",&n);
    while(n--){
        scanf("%d",&count);
        for ( i = 0; i < count; i++)
        {
            scanf("%d",&nums[i]);
        }
        for ( i = 0; i < count; i++)
        {
            scanf("%d",&nums[i+count]);
        }

        for ( i = 0; i < count*2-1; i++)
        {
            for ( j = 0; j < count*2-1-i; j++)
            {
                if(nums[j]>nums[j+1]){
                    int cnt=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=cnt;
                }
            } 
        }
        cnt=nums[0];
        printf("%d ",cnt);
        for ( i = 1; i < count*2; i++)
        {
            if(nums[i]!=cnt){
                cnt=nums[i];
                printf("%d ",cnt);
            }
        }
        
        printf("\n");
    }

    return 0;
}