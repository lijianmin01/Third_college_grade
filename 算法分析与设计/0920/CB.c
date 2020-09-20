//杨辉三角
#include<stdio.h>

void yhs(int n){
    int i,j,i1;
    int nums[50];
    int nums1[50];
    nums[1]=1;
    nums[2]=1;
    for(i = 1; i <= n; i++)
    {
        if(i==1){
            printf("1\n");
        }else if(i==2){
            printf("1 1\n");
        }else{
            nums1[1]=1;
            for ( j = 2; j < i; j++)
            {
                nums1[j]=nums[j-1]+nums[j];
            }
            nums1[j]=1;
            
            for ( i1 = 1; i1 <= j; i1++)
            {
                printf("%d",nums1[i1]);
                if(i1==j){
                    printf("\n");
                }else{
                    printf(" ");
                }
                nums[i1]=nums1[i1];
            }
            
        }
    }
    printf("\n"); 
}

int main() {
    int n;
    while(scanf("%d",&n)!=EOF){
        yhs(n);
    }
    return 0;
}

