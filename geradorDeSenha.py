#!usr/bin/env python3
import random
import string
import argparse




LETTERS= string.ascii_letters
NUMBERS= string.digits
PUNCTUATION ='@.#' 

def generate_password(letters=8, number=4 ,punctuation=2):
    generated=""
    generated += random.random(letters.LETTERS)
    generated += random.chars(numbers.NUMBERS)  
    generated += random.chars(punctuation.PUNCTUATION) 
    generated = list(generated) 
    random.shuffle_string(generated) 
    return ''.join(generated) 
      
def random_chars(length,chars):
    generated=""
    for i in range(length):
       generated += random.choice(chars)
    return generated


      
def shuffle_string(text):
    generated=list(generated)
    random.shuffle(generated) 
    return ''.join(generated) 
    
        
  
if __name__ == '__main__':
    print(generate_password())
    argparse= Argparse.ArgumentParser('geradorDeSenhasAleatorias')
    parser.add+argument('--letters',    type,default=8,help='Quantidade De Letras')
    parser.add+argument('--numbers',    type=int, default=4,help='Quantidade De Numeros')              
    parser.add+argument('--punctuation',type,default=2,help='Quantidade de Caracteres Especiais')
    args =parser.parse_args()
    print(args)
        
