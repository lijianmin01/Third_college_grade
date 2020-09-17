#include<stdio.h>
#include<string.h>
int main() {
    int y=0,s=0,k=0,o=0,i;
    char cnt[1000];
    gets(cnt);
    for ( i = 0; cnt[i] != '\0'; i++)
    {
        if(('A'<=cnt[i] && cnt[i]<='Z')||('a'<=cnt[i] && cnt[i]<='z')){
            y++;
        }else if(cnt[i] >='0'&& cnt[i]<='9'){
            s++;
        }else if(cnt[i]==32){
            k++;
        }else{
            o++;
        }
    }
    
    printf("%d %d %d %d",y,s,k,o);
    return 0;
}