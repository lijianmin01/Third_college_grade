#include<stdio.h>

int main(){
    int n;
    int count=0;
    scanf("%d",&n);
    int i,j,k;
    for ( i = 1; i < n/5; i++)
    {
        for ( j = 1; j < n/2 ; j++)
        {
            for ( k = 1; k < n; k++)
            {
                if((i*5+j*2+k)==n){
                    count++;
                }
            }   
        }
    }
    printf("%d\n",count);
    return 0;
}