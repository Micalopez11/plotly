# data_handler.py

import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        # Lee el archivo CSV con pandas al crear la instancia
        self.df = pd.read_csv(file_path)
        self.clean_data()

    def clean_data(self):
        # Elimina registros duplicados
        self.df.drop_duplicates(inplace=True)

        # Elimina filas con valores faltantes en columnas clave
        self.df.dropna(subset=['title', 'type', 'genres', 'releaseYear', 'imdbAverageRating'], inplace=True)

        # Convierte tipos de datos para asegurar que sean numéricos
        self.df['releaseYear'] = self.df['releaseYear'].astype(int)
        self.df['imdbAverageRating'] = self.df['imdbAverageRating'].astype(float)

    def get_titles_per_year(self):
        # Cuenta la cantidad de títulos publicados por año
        return self.df.groupby('releaseYear').size().reset_index(name='count')

    def get_average_rating_by_genre(self):
        # Divide los géneros (que están separados por comas) en filas distintas
        df_exploded = self.df.copy()
        df_exploded['genres'] = df_exploded['genres'].str.split(', ')
        df_exploded = df_exploded.explode('genres')

        # Calcula el promedio de rating por género
        return df_exploded.groupby('genres')['imdbAverageRating'].mean().reset_index()

    def get_type_distribution(self):
        # Cuenta cuántos títulos hay por tipo (Movie, TV Show, etc.)
        return self.df['type'].value_counts().reset_index(name='count').rename(columns={'index': 'type'})

    def get_rating_distribution(self):
        # Devuelve la columna de ratings para hacer un histograma
        return self.df['imdbAverageRating']
