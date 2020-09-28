#include<stdio.h>

int main(){
    int n,m;
    int cnt = 0;
    int nums[1010];
    int i,j;
    scanf("%d %d",&n,&m);
    for ( i = 0; i < m; i++)
    {
        scanf("%d",&nums[i]);
    }

    for ( i = 0; i < m-1; i++)
    {
        for ( j = 0; j < m-1-i; j++)
        {
            if(nums[j]>nums[j+1]){
                int temp =nums[j+1];
                nums[j+1]=nums[j];
                nums[j]=temp;
            }
        } 
    }

    int sum=0;
    for ( i = 0; i < m; i++)
    {
        sum += nums[i];
        if(sum<=n){
            cnt++;
        }else{
            break;
        }
    }
    
    printf("%d\n",cnt);
    
    return 0;
}