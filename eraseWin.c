#include <stdio.h>
int main(void){
    int nDigits;
    int nDigits2Erase;
    
    while (scanf("%d%d", &nDigits, &nDigits2Erase) == 2 && (nDigits || nDigits2Erase)){
  
        int i ,j , pos = 0;

        int posT = -1; //min

        char number[nDigits + 1];
        

        scanf("%s", number);

        char digitsOriginalOrder[nDigits + 1];

        //Converte o numberPresented em um array de ints
        //for(i = 0; i < nDigits2Erase; i++){
        while(nDigits2Erase > 0){
          
            
            if(posT == -1){
                digitsOriginalOrder[++posT] = number[pos++];
            
            }

            if(digitsOriginalOrder[posT] < number[pos]){
                posT--, nDigits2Erase--;
                //nDigits2Erase--;
            }
            else{
                //posT++;
                digitsOriginalOrder[++posT] = number[pos++];
                //pos++;
                if(pos == nDigits){
                    while(nDigits2Erase--){
                        posT--;
                    }
                }
            }
            
            
        }
        //Deleta a menor posicao
        for(j = pos; j < nDigits; j++){
          digitsOriginalOrder[++posT] = number[j];
        }
        digitsOriginalOrder[posT + 1] = '\0';

        printf("%s", digitsOriginalOrder);
        
        printf("\n");

    }
    
    return 0;
}
