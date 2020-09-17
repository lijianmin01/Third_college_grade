#include<stdio.h>

int main(){
    char strs[80];
    char strs1[80];
    gets(strs);
    int i;
    int cnt=0;
    for(i=0;strs[i];i++){
        if((strs[i]>='A'&&strs[i]<='Z')||(strs[i]>='a'&&strs[i]<='z')){
            strs1[cnt++]=strs[i];
        }
    }
    strs1[cnt]='\0';
    puts(strs1);
    return 0;
}