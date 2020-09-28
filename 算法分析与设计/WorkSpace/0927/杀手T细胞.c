#include<stdio.h>

int main(){
    int n,sum,cnt_1,cnt_2,sum_2,temp,cnt_3;
    while (scanf("%d",&n)!=EOF)
    {
        sum = 1;
        sum_2 = n/2;
        int i,j;
        for ( i = 1; i <= sum_2; i++)
        {
            cnt_1=n-2*i;
            cnt_2=i;
            int sum1=1,sum2=1;
            if(cnt_1>cnt_2){
                cnt_3=cnt_1;
                cnt_1++;
                for (j=0;j<cnt_2;j++)
                {
                    sum1*=(cnt_1--);
                    sum2*=(cnt_2--);
                }
                
            }else if(cnt_1<cnt_2){
                cnt_3=cnt_2;
                cnt_2++;
                for (j=0;j<cnt_1;j++)
                {
                    sum2*=(cnt_1--);
                    sum1*=(cnt_2--);
                }
            }else{
                //==
                cnt_3=cnt_1;
                cnt_1++;
                for (j=0;j<cnt_2;j++)
                {
                    sum1*=(cnt_1--);
                    sum2*=(cnt_2--);
                }
            }
            sum+=cnt_3+1+(sum1/sum2);
        }
        printf("%d\n",sum);
    }
    
    return 0;
}