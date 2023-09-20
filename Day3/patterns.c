// ****

#include <stdio.h>
int main()
{
    int i,j;
    // Pattern-1
// for (i=0;i<4;i++)
// {
//     // printf("*");
//     for (j=0;j<4;j++)
//     {
//         printf("*");
//         // j++;
//     }
//     printf("\n");
// }   

// Pattern - 2
// for (i=1;i<5;i++)
// {
//     for (j=1;j<=i;j++)
//     {
//         // printf("*");
//         // printf("%d",i);
//         printf("%d",j);

//     }
//     printf("\n");
// }

// Pattern -3

for (i=1;i<5;i++)
{
    for (j=1;j<=i;j++)
    {
        // printf("*");
        printf("%d",j);
    }
    printf("\n");
}
}
