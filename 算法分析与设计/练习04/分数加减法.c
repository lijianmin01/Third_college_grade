#include<stdio.h>
#include<string.h>

int func(int a,int b){
    int t,m,c;
    if(a<b){
        t = a;
        a = b;
        b = t;
    }
    m = a*b;
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
        char f;
        a = strs[0]-'0';
        b = strs[2]-'0';
        f=strs[3];
        c = strs[4]-'0';
        d = strs[6]-'0';

        int z,m,t;

        if(f=='+'){
        	int x,y;
        	x = a*d;
        	y = b*d;
            z = a*d + c*b;
            m = b*d;
            t = func(z,m);
            z /= t;
            m /= t;
            if(m!=1){
            	printf("%d/%d\n",z,m);
			}else{
				printf("%d\n",z);
			}
            
        }else{
            z = a*d - c*b;
            m = b*d;
            if(z==0){
                printf("0\n");
            }else{
                if(z>0){
                    t = func(z,m);
                    z /= t;
                    m /= t;
                    if(m!=1){
		            	printf("%d/%d\n",z,m);
					}else{
						printf("%d\n",z);
					}
            
                }else{
                    z *= (-1); 
                    t = func(z,m);
                    z /= t;
                    m /= t;
                    if(m!=1){
		            	printf("-%d/%d\n",z,m);
					}else{
						printf("-%d\n",z);
					}
                }
            }
        }
    }
    
    return 0;
}