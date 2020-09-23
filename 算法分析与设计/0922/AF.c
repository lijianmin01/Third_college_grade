#include<stdio.h>
#include<math.h>

int main(){
    int n,i,j,i1;
    int nums[10000];
    scanf("%d",&n);
    
    for ( i = 6; i <= n; i++)
    {
        int sum=1;
        int count=0;
        for ( j = 2; i <= sqrt(i); j++)
        {
            if(n%i==0){
                sum+=i;
                nums[j-2]=i;
                count++;
            }
        }
        
        if(sum==i){
            printf("%d its factors are ",i);
            for ( i1 = 0; i1 < count; i++)
            {
                printf("%d ",nums[i1]);
            }
            printf("\n");
        }
        
    }
    
    
    return 0;
}