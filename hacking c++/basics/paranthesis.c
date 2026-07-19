#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define MAX 100
char stack[MAX];
int top=-1;

void push(char data){
    if(top==MAX-1){
        printf("stack is full ");
        return;
    }
    else{
        top++;
        stack[top]=data;
    }
}

char pop(){
    char data;
    if(top==-1){
        printf("stack is empty");
        return 0;
    }
    else{
        data=stack[top];
        top--;
        return data;
    }
}

int matching_pair(char ch1,char ch2){
    if(ch1=='(' && ch2==')')
        return 1;
    else if(ch1=='{' && ch2=='}')
        return 1;
    else if(ch1=='[' && ch2==']')   // <- yaha galti thi 'ch2'
        return 1;
    else
        return 0;
}

int is_balanced(char *s){
    int i;
    for(i=0;i<strlen(s);i++){
        if(s[i]=='(' || s[i]=='{' || s[i]=='[')
            push(s[i]);
        else if(s[i]==')' || s[i]=='}' || s[i]==']'){
            if(top==-1){
                return 0;
            }
            else if(! matching_pair(pop(),s[i]))
                return 0;
        }
    }

    if(top==-1)
        return 1;
    else
        return 0;
}

int main(){
    char s[MAX];
    printf("enter the expression : ");
    scanf("%s",s);

    if(is_balanced(s))
        printf("the expression is balanced ");
    else
        printf("the expression is not balanced");

    return 0;
}
