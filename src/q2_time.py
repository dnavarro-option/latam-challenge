import pandas as pd
from typing import List, Tuple
import emoji

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON utilizando pandas para una carga rápida
    df = pd.read_json(file_path, lines=True)

    # Inicializamos un diccionario para contar los emojis
    emoji_counts = {}

    # Iterar rápidamente sobre las filas del DataFrame
    for content in df['content']:
        # Contar emojis en cada tweet
        for char in content:
            # Verificar si el carácter es un emoji utilizando la función is_emoji
            if emoji.is_emoji(char):
                if char in emoji_counts:
                    emoji_counts[char] += 1
                else:
                    emoji_counts[char] = 1

    # Ordenar los emojis por frecuencia y obtener los top 10
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_emojis
