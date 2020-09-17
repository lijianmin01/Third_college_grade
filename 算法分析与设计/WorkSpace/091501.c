#include<stdio.h>

int main() {
    int nums;
    int a,b,c,d,e,f;
    scanf("%d",&nums);
    int h[1000],m[1000],s[1000];
    int cnt=0;
    while(nums--){
        scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f);
        int flag=0;
        int q,w,e1;
        if(c+f>=60){
            flag=1;
            e1=(c+f)%60;
        }else{
            flag=0;
            e1=(c+f)%60; 
        }

        if(b+e+flag>=60){
            flag=1;
            w=(b+e+flag)%60;
        }else{
            flag=0;
            w=(b+e+flag);
        }

        q=a+d+flag;
        //printf("%d %d %d\n",q,w,e1);
        h[cnt]=q;
        m[cnt]=w;
        s[cnt]=e1;
        cnt++;
    }
    int i;
    for(i=0;i<cnt;i++){
        puts("%d %d %d",h[i],m[i],s[i]);
    }
    return 0;
}

