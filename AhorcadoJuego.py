import random

def ahorcado():
   
    palabras = ["amor", "llover", "llorar"]
  
    palabra = random.choice(palabras)
   
    letras_adivinadas = []
    intentos = 6  # Número máximo de intentos
    
    print("¡Bienvenido al juego del Ahorcado!")
    print("_ " * len(palabra))

       
        