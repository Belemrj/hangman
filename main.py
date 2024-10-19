import random
# Hacer una función que seleccione un palabra de un conjunto
palabras = ["manzana", "mango", "fresa"]
palabras2 = ["plátano", "uvas", "melón"]

def get_random_word(list):
    random_word = random.choice(list)
    return random_word
    
#ejemplo para utilizar la función
#get_random_word(palabras2)

#Crear una función para dar las instrucciones
#Adivina la palabra que tien x letras
def give_instructions(word):
    print("Vamos a jugar ahorcado")
    letters = str(len(word))
    print("Tu palabra tiene " + letters +" letras")

"""Ejemplo de ciclo
x = 1
while x <=  5:
    print(x)
    x = x + 1  
    """  

#Función que dibuje las líneas en forma horizontal, de acuerdo al número de letras contenidas en la palabra
def lines(word):
    final_string = ""
    letters = len(word)
    while letters > 0:
        final_string += " __ "
        letters -= 1
    print (final_string)

#Fnción para adivinar las letras
def guess(letter,word,guesses):
    print(letter)
    x = 0 
    final_string = ""
    while x < len(word):
        if word[x] == letter:
            final_string += letter
        elif word[x] in guesses:
            final_string += word[x]
        else: 
            final_string += " __ "
        x += 1


    print(final_string)    



def play():
    play_word = get_random_word(palabras)
    give_instructions(play_word)
    lines(play_word)
    chances = 10
    guesses = ""
    while chances > 0:
        response = input("Elige una letra: ")
        guess(response, play_word, guesses)
        guesses += response
        chances -= 1

play()