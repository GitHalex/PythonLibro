import time
import sys

# Cada línea con su velocidad por letra y el tiempo de espera antes de mostrarla
lyrics = [
    ("Quédate otra vez", 0.009, 0.0),
    ("Quédate toda la noche", 0.009, 5.0),
    ("Quédate a mi lado", 0.009, 6.0),
    ("Quédate más de las doce", 0.009, 6.0),
]


def animate_text(text, speed):
    """Muestra la línea letra por letra con un pequeño retardo."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Salto de línea


def sing_song():
    for line, speed, delay in lyrics:
        time.sleep(delay)  # Espera antes de empezar la línea
        animate_text(line, speed)


if __name__ == "__main__":
    sing_song()
