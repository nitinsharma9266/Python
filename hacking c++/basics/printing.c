#include<stdio.h>
int main(){

    int a;
    float b;
    char ch;
    printf("\n enter the value of an integer a : ");
    scanf("%d",&a);
    printf("\n enter the value of an float b : ");
    scanf("%f",&b);
    printf("\n enter the character : ");
    scanf("%c",&ch);
    printf("\n%d address of a=%u",&a);
    printf("\n%f address of b=%u",&b);
    printf("\n%c address of ch=%u",&ch);
    
return 0;
}