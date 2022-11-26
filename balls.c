#include <stdio.h>
#include <string.h>

int max(int num1, int num2)
{
    return (num1 > num2 ) ? num1 : num2;
}

//rows certo?
//cagada na alocacao de memoria *talvez
//2**9 -> 512 muito pouco(core dump)
//2**10 -> 1024 passa no teste
int integers[1024][1024] = {};
    //memset(integers, 0, rows*rows*sizeof(int));

int stackAux[1024][1024] = {};
    //memset(stackAux, 0, rows*rows*sizeof(int));

int stackTop[1024][1024] = {};
    //memset(stackTop, 0, rows*rows*sizeof(int));

int stack[1024][1024] = {};


int balls(int rows){
    int i, j, k;
    int integer;
    int sum, take = 0;
    
    //rows certo?
    //cagada na alocacao de memoria *talvez
    
    memset(stack, 0, sizeof(stack));

    //comecar pelo 1 ja que o 0 0 n tem bola em cima!
    for (i=1; i<= rows; i++){
      for(k = 1; k<= i; k++){
        scanf("%d", &integers[i][k]);
        //printf("check:%d", integers[i][k]);
        integers[i][k] += integers[i-1][k];

      }
    }
    for (i=1; i<= rows; i++){
      for(k = 1; k<= i; k++){
        stackAux[i][k] = integers[i][k] + stackAux[i-1][k-1];

      }
    }
    //memset(stack, 0, sizeof(stack));
    
    for (i=1; i<= rows; i++){
      for(k = i; k<= rows; k++){
        stack[k][i] = stackAux[k][i];

        stack[k][i] = max(stack[k][i], stackTop[k-1][i-1] + integers[k][i]);

        take = max(take, stack[k][i]);
        
      }
      
      stackTop[rows][i] = stack[rows][i];

      for(j = rows -1; j >= i; j--){
          stackTop[j][i] = max(stackTop[j+1][i], stack[j][i]);
   
       }
    }
    printf("%d", take);
    printf("\n");
}

int main(void){
    int rows;

    while(scanf("%d",&rows) == 1 && rows != 0){
      balls(rows);

    }
    return 0;
}
