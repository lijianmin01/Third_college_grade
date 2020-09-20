#include<stdio.h>

int main() {
    char passwords[120];
    gets(passwords);
    int i,len=0;
    for ( i = 0; passwords[i]!='\0'; i++){
        len++;
    }
    for ( i = 0; i<len-4; i++)
    {
        if('1'==passwords[i]||passwords[i]=='0'){
            printf("%c",passwords[i]);
        }else if('A'<=passwords[i]&&passwords[i]<='Z'){
            char cnt;
            cnt = passwords[i]-'A'+'a';
            if(cnt=='z'){
                cnt='a';
            }else{
                cnt++;
            }
            printf("%c",cnt);
        }else if('a'<=passwords[i]&&passwords[i]<='z'){
            int num;
            if(passwords[i]=='a'||passwords[i]=='b'||passwords[i]=='c'){
                num=2;
            }else if(passwords[i]=='d'||passwords[i]=='e'||passwords[i]=='f'){
                num=3;
            }else if(passwords[i]=='g'||passwords[i]=='h'||passwords[i]=='i'){
                num=4;
            }else if(passwords[i]=='j'||passwords[i]=='k'||passwords[i]=='l'){
                num=5;
            }else if(passwords[i]=='m'||passwords[i]=='n'||passwords[i]=='o'){
                num=6;
            }else if(passwords[i]=='p'||passwords[i]=='q'||passwords[i]=='r'||passwords[i]=='s'){
                num=7;
            }else if(passwords[i]=='t'||passwords[i]=='u'||passwords[i]=='v'){
                num=8;
            }else if(passwords[i]=='w'||passwords[i]=='x'||passwords[i]=='y'||passwords[i]=='z'){
                num=9;
            }
            printf("%d",num);
        }else{
            printf("%c",passwords[i]);
        }
    }
    for ( i = len-4; i < len; i++)
    {
        printf("%c",passwords[i]);
    }
    printf("\n");
    return 0;
}