#include <stdio.h>  
   
int main() {  
    int count, N, sum = 0;  
 
    printf("Enter a Positive Number\n");
 scanf("%d", &N);
   
    for(count = 1; count <= N; count++) {  
      
        if(count%2 == 0) { 
          
            sum = sum + count;  
        }  
    }
    printf("Sum of all Even numbers between 1 to %d is %d", N, sum);
 
    return 0;  
} 
