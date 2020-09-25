#include<stdio.h>
#include<string.h>

int main(){
    char str1[100],str2[100];
    int i=0,j=0,k,k1;
    while(gets(str1)){
        i=0,j=0;
        int count=0; //相同的长度
        int flag=0; //是否存在不同
        int len=0;//字符串原始长度
        int cnt=1;//字符串暂时长度
        int max=0;//字符串最大长度

        for ( i = 0; str1[i]!='\0'; i++)
        {
            len++;
        }

        int temp=0;
        for ( i = len-1; i >=0 ; i--)
        {
            str2[temp++]=str1[i];
        }
        
//        for ( i = len-1; i >=0 ; i--)
//        {
//            printf("%c %c\n",str1[i],str2[i]);
//        }
        
        if(len==1){
            printf("1\n");
        }else{
            for ( i = 0; i < len; i++)
            {
                k=i;
                for ( j = 0; j < len; j++)
                {
                	cnt=0;
                    for ( k1 = j; k1 < len; k1++)
                    {
                        if(str1[k]==str2[k1]){
                            cnt++;
                            if(max<cnt){
                                max=cnt;
                            }
                            k++;
                        }else{
                            cnt=0;
                            break;
                        }
                    }
                    
                } 
            }
            printf("%d\n",max);
        }


    }
    return 0;
}

