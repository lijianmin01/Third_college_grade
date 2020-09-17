#include<stdio.h>
#include<math.h>

int main(){
    int nums;
    scanf("%d",&nums);
    double x1,y1,x2,y2,x3,y3;
    double l1,l2,l3;
    double S;
    double a,b,c;
    while(nums){
        scanf("%lf %lf %lf %lf %lf %lf",&x1,&y1,&x2,&y2,&x3,&y3);
        a= (x1-x2)*(x1-x2)+((y1-y2)*(y1-y2));
        b = (x3-x2)*(x3-x2)+((y3-y2)*(y3-y2));
        c = ((x1-x3)*(x1-x3))+((y1-y3)*(y1-y3));
        l1 = sqrt(a);
        l2 = sqrt(b);
        l3 = sqrt(c);
        a=l1+l2;
        b=l1+l3;
        c=l2+l3;
        if ((a>l3)&&(b>l2)&&(c>l1)){
            S=1*1.0/4*sqrt((a+l3)*(a-l3)*(b-l2)*(c-l1));
            printf("%.3lf\n",S);
        }else{
            puts("Can not form a triangle.");
        }
        nums--;
    }
    return 0;
}