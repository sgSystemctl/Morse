string_to_morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
                   "k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.",
                   "s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..",
                   "0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
"""""
morse_to_string = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j",
                   "-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r",
                   "...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z",
                   "-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9"}
"""""

morse_to_string = { k:v for v,k in string_to_morse.items()}

#Conversione da stringa a morse
#In caso di caratteri speciali essi vengono ignorati e scartati


def conv_string_to_morse(msg:str,space:bool = True)->str:
    ret = ""
    for i in msg:
            
            #in caso di spazio basta accorparlo
            if i == " ":
                ret += i
            elif('a' <= i.lower() <= 'z' or '0' <= i <= '9'):
                ret += string_to_morse[i.lower()]
                ret += " " if space else ""
    return ret


def conv_morse_to_string(msg:str,space:bool = True)->str:
    ret = ""
    msg_list = msg.split(" ")
    for i in msg_list:
        if i == '':
            ret += " "
        elif i in morse_to_string.keys():
            ret += morse_to_string[i]
            ret += " " if space else ""
    
    return ret

if __name__ == "__main__":
    #costanti
    NUM_RIGHE = 54
    NUM_COLONNE = 15

    #stampa
    print("\n")
    print("-"*NUM_RIGHE)
    print("|"," "*NUM_COLONNE,"CONVERTITORE MORSE"," "*NUM_COLONNE,"|")
    print("-"*NUM_RIGHE)
    print("\n")

    rep = True
    while(rep):
        print("")
        print("1) Conversione Stringa to Morse")
        print("2) Conversione Morse to Stringa")
        print("3) fine")

        modalita = int(input("Scelta:"))

        if(modalita == 1):
            msg = input("Inserire la stringa da tradurre\n")
            print(conv_string_to_morse(msg))

        elif(modalita == 2):
            msg = input("Inserire il messaggio da tradurre\n")
            print(conv_morse_to_string(msg))
        
        elif(modalita == 3):
            print("Terminazione programma")
            print(conv_string_to_morse("Terminazione programma",False),":)")
            rep = False
        else:
            print("Modalità non supportata")
