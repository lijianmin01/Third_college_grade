// 问题 BP: 回文数

#include<stdio.h>
#include<string.h>
#include<cstdlib>

int panduan(int n){
    char nums[100];
    itoa(n,nums,10);
    int n_len=strlen(nums);
    int flag=1,i;
    for ( i = 0; i < n_len-1; i++)
    {
        if(nums[i]!=nums[n_len-i-1]){
            flag=0;
            break;
        }
    }
    // for ( i = 0; i < n_len-1; i++)
    // {
    //     printf("%c ",nums[i]);
    // }
    
    return flag;

}

int num_T(int n){
    char nums[100];
    char nums1[100];
    itoa(n,nums,10);
    int n_len=strlen(nums);
    int i,cnt=0,n1;
    for ( i = n_len-1; i >= 0; i--)
    {
        nums1[cnt++]=nums[i];
    }
    n1 = atoi(nums1);
    return n1;
    
}

int main(){
    //itoa() 将整型值转换为字符串。

    int n,i,j,cnt,num;
    scanf("%d",&n);
    while(n--){
        cnt = 0;
        scanf("%d",&num);
        if((num+num)<10){
            printf("1\n");
        }else{
            cnt++;
            num += num_T(num);
            while(!panduan(num)){
                cnt++;
                num += num_T(num);
                if(cnt>8){
                    cnt=0;
                    break;
                }
            }
            printf("%d\n",cnt);
        }
    }
    return 0;
}