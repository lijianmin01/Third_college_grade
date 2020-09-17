#include<stdio.h>
#include<string.h>

int main(){
    char strs[60];
    int m,i,j;
    char zi[10]="~!@#$%^";
    scanf("%d",&m);
    int count =m;
    gets(strs);
    while(m--){
        int flag=0;
        gets(strs);
        int len=0;
        for ( i = 0; strs[i]!='\0'; i++){
            len++;
        }
        if(8<=len&&len<=16){
            for ( i = 0; strs[i]!='\0'; i++)
            {
                if('A'<=strs[i]&&'Z'>=strs[i]){
                    flag++;
                    break;
                }
            }
            for ( i = 0;strs[i]!='\0'; i++)
            {
                if('a'<=strs[i]&&'z'>=strs[i]){
                    flag++;
                    break;
                }
            }
            for ( i = 0; strs[i]!='\0'; i++)
            {
                if('0'<=strs[i]&&'9'>=strs[i]){
                    flag++;
                    break;
                }
            }
            for ( i = 0; i < strs[i]!='\0'; i++)
            {
                int cnt=0;
                for (j = 0; zi[j]!='\0' ; j++)
                {
                    if(strs[i]==zi[j]){
                        cnt++;
                        flag++;
                        break;
                    }
                }
                if(cnt>0){
                    break;
                }
            }
            if(flag>=3){
                printf("YES\n");
            }else{
            printf("NO\n");
            }

        }else{
            printf("NO\n");
        }
        
        
    }
    return 0;
}