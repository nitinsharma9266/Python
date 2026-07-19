#include<stdio.h>
#define n 5
int stack[n];
int top=-1;
void push(int x){
    if (top==n-1){
        printf("stack is full");
    
    }
    else if(top==-1){
        top=0;
        stack[top]=x;
    }
    else{
        top++;
        stack[top]=x;
    }
}
int pop(){
        if(top==-1){
            printf("stack is empty\n");
        }
        else if(top==0){
            printf("stack top elemnts is=%d",stack[top]);
            top=-1;
        }
        else{
            printf("top elements is=%d",stack[top]);
            top--;
        }
}
int peek(){
    if(top==-1){
            printf("stack is empty\n");
        }
        else{
            printf("top elements is=%d",stack[top]);
        
        }
    
}
void display(){
    if(top==-1){
            printf("stack is empty\n");
        }
    else{
        int i;
        for(i=top;top<n;top++){
        printf("elements in stack is =%d",stack[i]);
    }
    }
}
int main(){
    int x;
    int choice;
    printf("enter your choice");
    scanf("%d",&choice);
   
    switch(choice){
        case 1:printf("enter element to be insert in the stack\n");
            scanf("%d",&x);
            push(x);
            break;
        case 2:pop();
            break;
        case 3:peek();
            break;
        case 4:display();
            break;
        case 5:return 0;
        default:printf("invalid choice");
    }   
}
