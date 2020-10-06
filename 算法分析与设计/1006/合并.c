#include<stdio.h>

int main(){
    int t1,t,n,cnt;
    int arr[300];
    int i,j;
    scanf("%d",&t1);
    while (t1--)
    {
        scanf("%d",&n);
        for ( i = 0; i < n*2; i++)
        {
            scanf("%d",&arr[i]);
        }

        for ( i = 0; i < n*2-1; i++)
        {
            for ( j = 0; j < n*2-1-i; j++)
            {
                if(arr[j]>arr[j+1]){
                    t = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = t;
                }
            }
        }
        printf("%d ",arr[0]);
        cnt=arr[0];
        for ( i = 1; i < n*2; i++){
            if(cnt!=arr[i]){
                cnt = arr[i];
                printf("%d",cnt);
                if((i+1)!=n*2){
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
    
    return 0;
}