#include<stdio.h>
#define Size 10
int arr[Size];
int top1=-1;
int top2=Size;

void push_stack1(int data){
    if(top1<top2-1){
        top1++;
        arr[top1]=data;
    }
    else{
        printf("stack full cannot push\n");
    }
}

void push_stack2(int data){
    if(top1<top2-1){
        top2--;
        arr[top2]=data;
    }
    else{
        printf("stack full cannot push\n");
    }
}

void pop_stack1(){
    if (top1>=0){
        int popped_value=arr[top1];
        top1--;
    }
    else{
        printf("stack empty cannot pop\n");
    }
}

void pop_stack2(){
    if (top2<Size){
        int popped_value=arr[top2];
        top2++;
    }
    else{
        printf("stack empty cannot pop\n");
    }
}

void print_stack1(){
    int i;
    for(i=top1;i>=0;i--){
        printf("%d ",arr[i]);
    }
    printf("\n");
}

void print_stack2(){
    int i;
    for(i=top2;i<Size;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}

int main(){
    int i;
    int num_of_ele;
    printf("we can push a total of 10 values in stack\n");

    for (i=1;i<=6;i++){
        push_stack1(i);
        printf("value pushed in stack 1 is %d\n",i);
    }

    for (i=1;i<=4;i++){
        push_stack2(i);
        printf("value pushed in stack 2 is %d\n",i);
    }

    print_stack1();
    pop_stack2();

    printf("pushing value in stack 1 is %d\n",11);
    push_stack1(11);

    num_of_ele=top1+1;
    while(num_of_ele){
        pop_stack1();
        --num_of_ele;
    }

    pop_stack1();
    return 0;
}
