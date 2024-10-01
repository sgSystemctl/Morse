#include <iostream>
#include <string>
#include <cstring>
using namespace std;

#define MAX_LEN 255


int main(){
    string alfabeto[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",
                      ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                      "...","-","..-","...-",".--","-..-","-.--","--.."};
                                            
    string numeri[] = {"-----",".----","..---","...--","....-",".....","-....","--...","---..","----."};
    
    char input[MAX_LEN];
    memset(input,0,MAX_LEN);
    
    int scelta = 0;
    bool rip = true;

    while (rip)
    {
            
        cout<<"####TRADUTTORE MORSE####"<<endl;
        cout<<"1) Da lettere a morse"<<endl;
        cout<<"2) Da morse a lettere"<<endl;
        cout<<"3) exit"<<endl;
        
        fgets(input,MAX_LEN,stdin);
        scelta = atoi(input);
    
    
        switch (scelta)
        {

            case 1:
            {
                memset(input,0,MAX_LEN);
                cout<<"Inserire la parola: ";
                fgets(input,MAX_LEN,stdin);
                cout<<input<<endl;
                //traduzione
                for (int i = 0;i < MAX_LEN && input[i] != '\0';i++){
                    
                    if(input[i] >= '0' && input[i] <= '9'){
                        int temp = input[i] - '0';
                        cout<<input[i]<<": "<<numeri[temp]<<endl;
                    } 

                    input[i] |= 32;//faccio il lowercast della parola
                    if(input[i] >= 'a' && input[i] <= 'z'){
                        int temp = input[i]-'a';
                        cout<<input[i]<<": "<<alfabeto[temp]<<endl;
                    }

                    
                }
                cout<<endl;
                break;
            }

            case 2:
            {

                break;
            }

            case 3:
                rip = false;
                break;
            
            default:
                cout<<"Scelta non valida"<<endl;
                break;
        }
    }

}