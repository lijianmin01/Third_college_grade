#include<stdio.h>
#include<string.h>

int main(){
    int n;
    scanf("%d",&n);
    char str1[10002];
    char str2[10002];
    int len,index,i,flag=0;
    while(n--){
        index=1;
        flag=0;
        scanf("%s",str1);
        len=strlen(str1);
        //printf("%d\n",len);
        str2[0]=str1[0];
        for ( i = 1; i < len; i++)
        {
            if(str1[i]=='('||str1[i]=='['||str1[i]=='{'||str1[i]=='<'){
                str2[index++]=str1[i];
            }else if(str1[i]==')'){
                if(str2[index-1]=='('){
                    index--;
                }else{
                    flag=1;
                    break;
                }
            }else if(str1[i]==']'){
                if(str2[index-1]=='['){
                    index--;
                }else{
                    flag=1;
                    break;
                }
            }else if(str1[i]=='}'){
                if(str2[index-1]=='{'){
                    index--;
                }else{
                    flag=1;
                    break;
                }
            }else if(str1[i]=='>'){
                if(str2[index-1]=='<'){
                    index--;
                }else{
                    flag=1;
                    break;
                }
            }
        }
        // if(flag==1){
        //     printf("No\n");
        // }else if(index==1){
        //     printf("No\n");
        // }else{
        //     printf("Yes\n");
        // }
        if(flag==0&&index==0){
            printf("Yes\n");
        }else{
            printf("No\n");
        }
    }
    return 0;
}