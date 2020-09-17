#include<stdio.h>

int main(){
    int nums1[120];
    int nums2[120];
    int n,i,j,cnt;
    scanf("%d",&n);
    for ( i = 0; i < n; i++)
    {
        scanf("%d",&nums1[i]);
    }

    for ( i = 0; i < n-1; i++)
    {
        for (j  = 0; j < n-1-i; j++)
        {
            if(nums1[j]>nums1[j+1]){
                cnt = nums1[j+1];
                nums1[j+1] = nums1[j];
                nums1[j] = cnt;
            }
        }
    }

    nums2[0]=nums1[0];
    int count =1;
    for(i=1;i<n;i++){
        if(nums1[i]!=nums2[count-1]){
            nums2[count++]=nums1[i];
        }
    }
    
    printf('%d\n',count);
    for ( i = 0; i < count; i++)
    {
        printf("%d ",nums2[i]);
    }
    
    

    return 0;
}