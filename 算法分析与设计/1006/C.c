#include<stdio.h>

int main(){
    // 0 关闭  1 打开
    int n,k;
    int arr[1001];
    int i,j;
    scanf("%d %d",&n,&k);
    for ( i = 1; i < n+1; i++)
    {
        arr[i]=1;
    }
    for(j=2;j<=k;j++){
        for ( i = 1; i < n+1; i++){
            if(i%j==0){
                arr[i]=(arr[i]+1)%2;
            }
        }
    }
    for ( i = 1; i < n+1; i++){
        if(arr[i]==1){
            printf("%d ",i);
        }
    }
    return 0;
}