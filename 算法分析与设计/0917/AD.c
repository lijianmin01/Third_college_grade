//问题 AG
#include<stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int nums1[1000];
    int nums2[1000];
    nums1[1]=2;
    nums1[2]=3;
    int i;
    for ( i = 3; i < n+1; i++)
    {
        nums1[i]=nums1[i-1]+nums1[i-2];
    }

    nums2[1]=1;
    nums2[2]=2;
    for ( i = 3; i < n+1; i++)
    {
        nums2[i]=nums2[i-1]+nums2[i-2];
    }
    
    
    double sum=0;
    for ( i = 1; i < n+1; i++)
    {
        //printf("%d %d\n",nums1[i],nums2[i]);
        sum+=nums1[i]*1.0/nums2[i]*1.0;
    }
    printf("%.2f\n",sum);
    
    return 0;
}