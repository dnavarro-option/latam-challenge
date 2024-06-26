import pandas as pd
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON utilizando pandas para una carga rápida
    df = pd.read_json(file_path, lines=True)

    # Inicializamos un diccionario para contar las menciones por usuario
    mention_counts = {}

    # Iterar rápidamente sobre las filas del DataFrame
    for mentions in df['content'].str.findall(r'@\w+'):
        for mention in mentions:
            # Actualizar el contador de menciones
            if mention in mention_counts:
                mention_counts[mention] += 1
            else:
                mention_counts[mention] = 1

    # Obtener los top 10 usuarios más mencionados
    top_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_mentions
