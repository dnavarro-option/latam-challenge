import json
from collections import defaultdict
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Utilizamos defaultdict para contar menciones eficientemente
    mention_counts = defaultdict(int)

    # Abrimos el archivo en modo lectura y procesamos línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            # Buscar menciones en el contenido
            mentions = [word for word in content.split() if word.startswith('@')]
            for mention in mentions:
                mention_counts[mention] += 1

    # Obtener los top 10 usuarios más mencionados
    top_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_mentions
