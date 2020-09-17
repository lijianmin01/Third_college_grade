//问题 BJ: 【C语言训练】字符串正反连接

#include<stdio.h>
#include<string.h>

int main(){
    char strs[150];
    char strs1[150];
    gets(strs);
    int i,nums=0;
    for ( i = 0; strs[i]!='\0'; i++)
    {
        nums++;
        strs1[i]=strs[i];
    }
    int cnt=nums;
    for ( i = nums-1; i>=0; i--)
    {
        strs1[cnt++]=strs[i];
    }
    strs1[2*nums]='\0';
    puts(strs1);
    
    return 0;
}