from data_handler import DataHandler
from visualizer import Visualizer

handler = DataHandler('data.csv')
viz = Visualizer()

df = handler.get_titles_per_year()
viz.plot_titles_per_year(df)

# grafico_rating_por_genero.py

from data_handler import DataHandler
from visualizer import Visualizer

data_path = 'data.csv'

handler = DataHandler(data_path)
viz = Visualizer()

# Gráfico: promedio de rating por género
df = handler.get_average_rating_by_genre()
viz.plot_avg_rating_by_genre(df)

# grafico_tipo_contenido.py

from data_handler import DataHandler
from visualizer import Visualizer

data_path = 'data.csv'

handler = DataHandler(data_path)
viz = Visualizer()

# Gráfico: distribución por tipo de contenido
df = handler.get_type_distribution()
df['type'] = df['type'].str.strip().str.lower()  # Limpia espacios y pone en minúsculas
df['type'] = df['type'].replace({'movie': 'Películas', 'tv': 'Series'})
viz.plot_type_distribution(df, title="Distribución de tipos de contenido")

# grafico_distribucion_ratings.py

from data_handler import DataHandler
from visualizer import Visualizer

data_path = 'data.csv'

handler = DataHandler(data_path)
viz = Visualizer()

# Gráfico: distribución de ratings
series = handler.get_rating_distribution()
viz.plot_rating_distribution(series, title="Distribución de ratings IMDB en Netflix", x_label="Puntaje IMDB", y_label="Cantidad de títulos")