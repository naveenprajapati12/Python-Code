#include <stdio.h>

int main()
{int a[10],i,pos=2,temp;
 int ele=10,n;
    printf("Enter the size of the array : ");
    scanf("%d",&n);
    printf("enter the arr is:");
    for(i=0; i <n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=n-1;i>=pos;i--)
    {
      a[i+1]=a[i];
    }
     a[pos]=ele;
    


   printf("The array is : ");
   for(int i=0;i<=n;i++){
       printf("%d \t",a[i]);
   }

    return 0;
}