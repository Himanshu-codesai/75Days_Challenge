#include <stdio.h>

int main()
{
    int choice;
    printf("enter nu \n");
    scanf("%d",&choice);
    
    switch (choice)
    {
    case 1:
        printf("choice is 1");/* code */
        break;
    case 2:
        printf("choice is 2");
        break;
    
    default:
        printf("default choice is -> %d",choice);
    }
}