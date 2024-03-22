import random

def get_word_displayed(difficulty, secret_word, guessed_letters):
    word = []
    if difficulty == 1:
        for letter in secret_word:
            if letter in 'aeiou':
                guessed_letters.append(letter)
                word.append(letter)
            else:
                word.append("_")
        return word
    elif difficulty == 2:
        guessed_letters.append(secret_word[0])
        guessed_letters.append(secret_word[-1])
        for letter in secret_word:
            if letter in guessed_letters:
                word.append(letter)
            else:
                word.append("_")
        return word
    elif difficulty == 3:
        word = ["_" for _ in secret_word]
        return word

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 10

# Contador de intentos
attempts = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

print("--------------------")
print("Dificultades: ")
print("1. Facil")
print("2. Media")
print("3. Dificil")
difficulty = int(input("Ingrese una dificultad: "))

word_displayed = "".join(get_word_displayed(difficulty, secret_word, guessed_letters))

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while attempts < max_attempts:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if not letter:
       print("Valor invalido. Por favor, ingresa una letra.")
       continue
     
    # Verificar que se ingrese una letra
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        attempts += 1
        print("Lo siento, la letra no está en la palabra.")
        print(f"{attempts} intentos fallidos de {max_attempts}")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")