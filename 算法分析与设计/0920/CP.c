#include<stdio.h>

int main(){
    int m,n;
    int cnt,key;
    scanf("%d %d",&n,&m);
    int i,j;
    //先算一共y有多少数
    // int c1,c2,count;
    // c1=1;
    // c2=1;
    // for(i=n;i>=m;i++){
    //     c1*=i;
    // }
    // for ( i = 1; i <= m; i++)
    // {
    //     c2*=i;
    // }
    // count = c1/c2;

    cnt = n;
    i = 1;
    key = 1;


    int nums[300];
    int nums1[300];
    int ind[300];
    for ( i = 0; i < m; i++)
    {
        nums[i]=0;
    }

    nums[0]=key;
    nums1[0]=key;
	ind[0]=key; 
    for ( i = 1; i < m; i++)
    {
        nums[i]=nums[i-1]+1;
        nums1[i]=nums[i];
        ind[i]=nums[i];
    }

    for ( i = 0; i < m; i++)
    {
        printf("%d",nums[i]);
        if(i+1!=m){
            printf(" ");
        }else{
            printf("\n");
        }
    }
    
    while(1){
        int index = m;
        nums[m-1]++;
        for ( i = 0; i < m; i++)
        {
            printf("%d",nums[i]);
            if(i+1!=m){
                printf(" ");
            }else{
                printf("\n");
            }
        }
        for ( i = m-1; i > 0; i--)
        {
            if(ind[i]==n-(m-1-i)){
                ind[i-1]++;
                ind[i]=nums1[i];
            }
        }
        if(ind[0]==1){
            break;
        }
    }

    return 0;
}


