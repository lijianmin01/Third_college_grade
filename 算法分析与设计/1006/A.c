#include<stdio.h>

int main(){
    int arr[6];
    int i,j,t;
    for ( i = 0; i < 6; i++)
    {
        scanf("%d",&arr[i]);
    }

    for ( i = 0; i < 6-1; i++)
    {
        for ( j = 0; j < 5-i; j++)
        {
            if(arr[j]<arr[j+1]){
                t = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = t;
            }
        }
    }
    if(arr[0]==0){
        printf("0");
        return 0;
    }
    for(i=0;i<6;i++){
        printf("%d",arr[i]);
    }
    
    return 0;
}