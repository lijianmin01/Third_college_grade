#include<stdio.h>
#include<string.h>

int func(int a,int b){
    int t,m,c;
    if(a<b){
        t = a;
        a = b;
        b = t;
    }
    c = a%b;
    while(c!=0){
        a = b;
        b = c;
        c = a%b;
    }
    return b;
}

int main(){
    char strs[10];
    while (scanf("%s",strs)!=EOF)
    {
        int a,b,c,d;
        a = strs[0]-'0';
        b = strs[2]-'0';
        c = strs[4]-'0';
        d = strs[6]-'0';

        int z,m;
        if(strs[3]=='-'){
            int flag=1;//分子是否为负数
            z = a*d-b*c;
            m = b*d;
            if(z<0){
                z *= (-1);
                flag=-1;
            }
            if(z==0){
                printf("0\n");
            }else{
                if(z%m==0){
                    printf("%d\n",z/m);
                }else{
                    int cnt=func(z,m);
                    z /= cnt;
                    m /= cnt;
                    printf("%d/%d\n",z*flag,m);
                }
            }

        }else{
            z = a*d+b*c;
            m = b*d;
            if(z%m==0){
                printf("%d\n",z/m);
            }else
            {
                int cnt=func(z,m);
                z /= cnt;
                m /= cnt;
                printf("%d/%d\n",z,m);
            }
        }
    }
    
    return 0;
}