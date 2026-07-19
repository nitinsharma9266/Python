#include<stdio.h>
void main(){
    int x;
    printf("enter the value of x : ");
    scanf("%d",&x);
    printf("\n value of x :%d",x);
    printf("\n address of x : %u",&x);
    printf("\n value of adress %u=%d",&x,*(&x));
    
}