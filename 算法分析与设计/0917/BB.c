// #include<stdio.h>
// #include<string.h>

// int main() {
//     int n,n1,n2;
//     scanf("%d",&n);
//     if(n==0){
//         printf("0 0 0\n");
//         return 0;
//     }
//     n1=n;
//     n2=n;
//     char sno[1];
//     char name[6];
//     double a,b,c;

//     double sum1=0,sum2=0,sum3=0,cnt=0;

//     char sno1[20];
//     char name1[20];
//     double a1,b1,c1;
	
//     scanf("%s %s %lf %lf %lf",sno,name,&a,&b,&c);
    
//     //printf("%s %s %d %d %d\n",sno,name,a,b,c);

//     strcpy(sno1,sno);
//     strcpy(name1,name);
//     a1=a;
//     b1=b;
//     c1=c;

//     sum1=a;
//     sum2=b;
//     sum3=c;

//     cnt =a+b+c;
//     n1--;
//     while(n1--){
//          scanf("%s %s %lf %lf %lf",sno,name,&a,&b,&c);

//         sum1+=a*1.0;
//         sum2+=b*1.0;
//         sum3+=c*1.0;

//         if(cnt<(a+b+c)){
//             strcpy(sno1,sno);
//             strcpy(name1,name);
//             a1=a;
//             b1=b;
//             c1=c;
//         }
        
//     }
//     printf("%.0f %.0f %.0f \n",sum1/n2,sum2/n2,sum3/n2);
//     printf("%s %s %.0f %.0f %.0f",sno1,name1,a1,b1,c1);

//     return 0;
// }



#include<stdio.h>
#include<stdlib.h>

struct node{
	char number;
	char name;
	int grade1;
	int grade2;
	int grade3;
	
	struct node *next;
};

struct node *first=NULL;

void insert(){
	struct node *new_node;
	
	new_node=(struct node *)malloc(sizeof(struct node));
	
	//printf("请输入学生信息及成绩（格式：x x x x x）：");
	scanf("%s %s %d %d %d",&new_node->number,&new_node->name,&new_node->grade1,&new_node->grade2,&new_node->grade3);

	
	new_node->next=first;
 	first=new_node;
	
}


void print(int n){
	struct node *p;
	
	int max;
	int k;
	char number;
	int grade=0;
	int grade1=0;
	int grade2=0;
	int grade3=0;

	int i;
	
	for(p=first,i=1;p!=NULL;p=p->next,i++){
		grade=p->grade1 + p->grade2 + p->grade3;
		//printf("学号：%c 姓名：%c 平均成绩：%d \n",p->number,p->name,(grade/3));
		grade1=grade1+p->grade1;
		grade2=grade2+p->grade2;
		grade3=grade3+p->grade3;
		k=grade/3;
		if(max<k){
			max=k;
			number=p->number;
		}
	}
	//printf("平均分最高的学生的学号为%c 平均成绩为%d \n",number,max);
	
	printf("%d ",(grade1/n));
	printf("%d ",(grade2/n));
	printf("%d\n",(grade3/n));
}


int main(){
	
	
	int i,n;
	//printf("请输入要插入学生的人数");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		//printf("请输入学生%d的信息\n",i+1);
		insert();
	}
	
	print(n);
}

