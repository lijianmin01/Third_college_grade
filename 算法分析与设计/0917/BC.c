#include <stdio.h>
typedef struct student
{
    int num;
    double grade;
    struct student *next;
} student;

student *merge(student *a, student *b)
{
    //先合并，后排序
    student *head = a;
    while (a->next != NULL)
    {
        a = a->next;
    }
    a->next = b;
	//选择排序，每次选最小的，放在未排序的链表头部
    student *pre;
    pre = head;
    while (pre->next != NULL)
    {
        a = pre->next;
        while (a != NULL)
        {
            if (pre->num > a->num)
            {
                int num = pre->num;
                double grade = pre->grade;
                pre->num = a->num;
                pre->grade = a->grade;
                a->num = num;
                a->grade = grade;
            }
            a = a->next;
        }
        pre = pre->next;
    }
    return head;
}

int main()
{
    

    int n,m;
    scanf("%d %d",&n,&m);
    student a[n];
    student b[m];
    int i,num_cnt;
    double grade_cnt;
    for ( i = 0; i < n; i++)
    {
        scanf("%d %lf",&num_cnt,&grade_cnt);
        a[i].num=num_cnt;
        a[i].grade=grade_cnt;
        a[i].next = &a[i+1];
    }
    a[n-1].next=NULL;

    for ( i = 0; i < m; i++)
    {
        scanf("%d %lf",&num_cnt,&grade_cnt);
        b[i].num=num_cnt;
        b[i].grade=grade_cnt;
        b[i].next = &b[i+1];
    }
    b[m-1].next=NULL;
    
    student *combine = merge(a, b);
    while (combine != NULL)
    {
        printf("%d %.0lf\n", combine->num, combine->grade);
        combine = combine->next;
    }

    return 0;
}