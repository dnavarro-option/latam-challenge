import json
from collections import defaultdict
from typing import List, Tuple
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Utilizamos defaultdict para contar emojis eficientemente
    emoji_counts = defaultdict(int)

    # Abrimos el archivo en modo lectura y procesamos línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            # Contar emojis en cada tweet
            for char in content:
                # Verificar si el carácter es un emoji utilizando la función is_emoji
                if emoji.is_emoji(char):
                    emoji_counts[char] += 1

    # Obtener los top 10 emojis más comunes
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_emojis
