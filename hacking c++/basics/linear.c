#include<stdio.h>
void main()
{
int a[6]={5,7,2,8,9};
int item ;
int i;
int count=0;
printf("enter element to be searched : ");
scanf("%d",&item);
for (i=0;i<6;i++){
    if (a[i]==item){
        printf("found element at location i=%d ",i);
        count++;
    }
    
    }
if(count==0){
    printf("not found");
}
}

