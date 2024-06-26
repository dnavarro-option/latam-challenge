import json
from collections import defaultdict, Counter
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Utilizamos defaultdict para contar fechas y usuarios eficientemente sin necesidad de verificar la existencia de las claves.
    date_counts = defaultdict(int)
    user_counts = defaultdict(lambda: defaultdict(int))

    # Abrimos el archivo en modo lectura y procesamos línea por línea.
    with open(file_path, 'r') as file:
        for line in file:
            # Parseamos cada línea como un objeto JSON.
            tweet = json.loads(line)
            # Extraemos la fecha y el nombre de usuario del tweet.
            date = datetime.fromisoformat(tweet['date']).date()
            username = tweet['user']['username']
            # Incrementamos el contador para la fecha y para el usuario en esa fecha.
            date_counts[date] += 1
            user_counts[date][username] += 1

    # Obtenemos las 10 fechas con más tweets utilizando Counter para contar y ordenar eficientemente.
    top_dates = [date for date, count in Counter(date_counts).most_common(10)]
    result = []
    for date in top_dates:
        # Para cada fecha en el top 10, encontramos el usuario con más tweets.
        top_user = max(user_counts[date], key=user_counts[date].get)
        result.append((date, top_user))
    
    return result
