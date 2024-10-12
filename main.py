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

def play():
    play_word = get_random_word(palabras)
    give_instructions(play_word)

play()