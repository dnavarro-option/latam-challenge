import pandas as pd
from datetime import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo JSON línea por línea
    df = pd.read_json(file_path, lines=True)
    
    # Convertir la columna 'date' a formato de fecha
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    # Obtener las 10 fechas con más tweets
    top_dates = df['date'].value_counts().nlargest(10).index
    
    result = []
    for date in top_dates:
        # Encontrar el usuario con más tweets en esa fecha
        user = df[df['date'] == date]['user'].apply(lambda x: x['username']).value_counts().idxmax()
        result.append((date, user))
    
    return result