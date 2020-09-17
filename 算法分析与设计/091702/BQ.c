#include<stdio.h>
int f(int i){
    if(i>=0){
        return i;
    }else{
        return i*(-1);
    }
}

int main(){
    int n;
    int nums[120];
    int i,j,cnt;
    scanf("%d",&n);
    while(n!=0){
        for ( i = 0; i < n; i++)
        {
            scanf("%d",&nums[i]);
        }
        for(i=0;i<n-1;i++){
            for(j=0;j<n-1-i;j++){
                if(f(nums[j])<f(nums[j+1])){
                    cnt=nums[j+1];
                    nums[j+1]=nums[j];
                    nums[j]=cnt;
                }
            }
        }
        for ( i = 0; i < n; i++)
        {
            printf("%d ",nums[i]);
        }
        printf("\n");
        scanf("%d",&n);
    }
    return 0;
}