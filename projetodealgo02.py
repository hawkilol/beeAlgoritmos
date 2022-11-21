# -*- coding: utf-8 -*-
"""ProjetoDeAlgo02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zM6FzNdcusGdP2pS0aPwR1UOKEE4J93R
"""

import time
import matplotlib.pyplot as plt
import numpy as np

#Q1

#heapsort
def heapify(arr,n,i):#peneira
  largest = i
  l = 2*i + 1
  r = 2*i + 2

  if l < n and arr[largest].t < arr[l].t:
    largest = l
  
  if r < n and arr[largest].t < arr[r].t:
    largest = r
  
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    #arr[i] = arr[largest]
    #arr[largest] = arr[i]

    heapify(arr,n,largest)

def heapSort(arr):
  n = len(arr)
  
  for i in range(n//2 -1,-1,-1):
    heapify(arr,n,i)
  
  for i in range(n-1,0,-1):
    arr[i], arr[0] = arr[0], arr[i]
    
    heapify(arr,i,0)



def sumTimes(clienteTimes):
  sum = 0;
  #clienteTimes = [3,5,10]
  
  sumAux =0

  for i in clienteTimes:
    print(i.t)
    sum += i.t  
    #sum +=i
    #print(sum)
    
    sumAux += sum

  print("Soma Minima: ")
  print(sumAux)
  return sumAux

#Q1

import copy
#versao objeto
class cliente:
  def __init__(self):
    self.n = None
    self.t = 0

def schedule():
  nCliente = cliente()
  nClientes = int(input("Numero de clientes:"))

  clienteTimes = []
  minimi = 0
  mini = 0
  
  for i in range(1, nClientes +1):
    clientN = "TempoCliente " + str(i) +": "
    
    nCliente.n = i
    time = int(input(clientN))

    nCliente.t = time

    clienteAux = copy.deepcopy(nCliente)

    clienteTimes.append(clienteAux)


  #heapsort O(n log n)
  heapSort(clienteTimes)
  
  
  sumTimes(clienteTimes)

  r = ""
  for i in clienteTimes:
    r+=str(i.n)

  print("Ordem: " + r)

  #print(clienteTimes.pop(0))

schedule()

# %%writefile Q1.c
# #include <stdio.h>
# int santaBag(int toys, int weight, int weightLimit){

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# ls
# gcc Q1.c -o Q1
# ./Q1



#Q2 http://www.beecrowd.com.br/judge/pt/problems/view/1767

#Incompleto n compilou :(

#Q3 http://www.beecrowd.com.br/judge/pt/problems/view/1312



#rightversion refazer

#%%writefile Q3.c
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

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# ls
# gcc Q3.c -o Q3
# ./Q3

#Q4 http://www.beecrowd.com.br/judge/pt/problems/view/1084

#V2 pra rodar mas rapido

# Commented out IPython magic to ensure Python compatibility.
# %%writefile Q4.c
# #include <stdio.h>
# #include <stdlib.h>
# #include <time.h>
# #include <math.h>
# 
# int winning(int nDigits, int nDigits2Erase, int numberPresented){
#     
#     int arrLen = nDigits + 1;
#     char arr[arrLen];
#     int i, j, intResult, posRemove  = 0;
#     int array[nDigits];
#     
#     //Converte o numberPresented em um array de ints
#     snprintf(arr, nDigits + 1, "%d", numberPresented);
#     for(i = 0; i< nDigits; i++){
#         
#         array[i] = arr[i] - '0';
#         
#     }
# 
#    
#     int min = array[0];
#     
# 
#     //remove os menores ints nDigits2Erase vezes
# 
#     for(i = 0; i<nDigits2Erase; i++){
#         
#         //Escolhe os menor int
#         min = array[0];
#         for(int j = 0; j< nDigits; j++){
#             
#             if(array[j]< min){
#                 min = array[j];
#                 //Acha a pos do menor 
#                 posRemove = j; 
# 
#             }
#             
#         }
# 
# 
#         //Acha a pos do menor 
#        
#         
#         //Remove o menor int reconstruindo a lista sem ele 
#         
#         
#         //posRemove++;
#         for(j = posRemove; j < nDigits-1 ; j++){
#   
#             array[j] = array[j + 1];
#                 
#         }
# 
#         nDigits--;
#         
#     }
#     
# 
#     for(i=0; i<nDigits; i++){
#             intResult = intResult*10 + array[i];
#     }
#     return intResult;
#     
#     
# }
#     
# 
# int main(int argc, char *argv[]){
#     int nDigits;
#     int nDigits2Erase;
#     int numberPresented;
# 
#     clock_t start;
#     clock_t stop;
#     double end;
# 
#     //scanf("%d %d", &nDigits, &nDigits2Erase);
#     
#     while (scanf("%d%d", &nDigits, &nDigits2Erase) == 2 && (nDigits || nDigits2Erase)){
#       scanf("%d", &numberPresented);
# 
#       start = clock();
#       int r = winning(nDigits, nDigits2Erase, numberPresented);
#       printf("%d", r);
#       printf("\n");
#       stop = clock();
#       end = (double) (stop - start) / CLOCKS_PER_SEC;
#       printf("%f", end);
# 
#     }
#     
#     
#     
# 
#     return 0;
# }
#

#semFunc (+ rapido?)

#ACCEPTED! OBS: teve q ser super otimizado pra passar no timelimit 1

# Commented out IPython magic to ensure Python compatibility.
# %%writefile Q4.c
# #include <stdio.h>
# int main(void){
#     int nDigits;
#     int nDigits2Erase;
#     
#     while (scanf("%d%d", &nDigits, &nDigits2Erase) == 2 && (nDigits || nDigits2Erase)){
#   
#         int i ,j , pos = 0;
# 
#         int posT = -1; //min
# 
#         char number[nDigits + 1];
#         
# 
#         scanf("%s", number);
# 
#         char digitsOriginalOrder[nDigits + 1];
# 
#         //Converte o numberPresented em um array de ints
#         //for(i = 0; i < nDigits2Erase; i++){
#         while(nDigits2Erase > 0){
#           
#             
#             if(posT == -1){
#                 digitsOriginalOrder[++posT] = number[pos++];
#             
#             }
# 
#             if(digitsOriginalOrder[posT] < number[pos]){
#                 posT--, nDigits2Erase--;
#                 //nDigits2Erase--;
#             }
#             else{
#                 //posT++;
#                 digitsOriginalOrder[++posT] = number[pos++];
#                 //pos++;
#                 if(pos == nDigits){
#                     while(nDigits2Erase--){
#                         posT--;
#                     }
#                 }
#             }
#             
#             
#         }
#         //Deleta a menor posicao
#         for(j = pos; j < nDigits; j++){
#           digitsOriginalOrder[++posT] = number[j];
#         }
#         digitsOriginalOrder[posT + 1] = '\0';
# 
#         printf("%s", digitsOriginalOrder);
#         
#         printf("\n");
# 
#     }
#     
#     return 0;
# }

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# ls
# gcc Q4.c -o Q4
# ./Q4

