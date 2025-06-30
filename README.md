# Proyecto de Visualización de Contenido de Netflix con Plotly y POO

Este proyecto aplica los principios de Programación Orientada a Objetos (POO) para visualizar datos del catálogo de Netflix utilizando la biblioteca Plotly. Permite explorar y analizar la distribución de títulos, tipos de contenido y calificaciones de IMDb de manera interactiva.

## Estructura del Proyecto

```
project/
├── data.csv           # Datos de Netflix (proporcionado)
├── main.py            # Punto de entrada del programa
├── data_handler.py    # Clase para carga y procesamiento de datos
├── visualizer.py      # Clase para generar gráficos
└── README.md          # Instrucciones del proyecto
```

## Descripción del Dataset

El archivo `data.csv` contiene información sobre títulos de Netflix, incluyendo las siguientes columnas principales:
- `title`: Nombre del título
- `type`: Película o serie
- `genres`: Géneros asociados
- `releaseYear`: Año de lanzamiento
- `imdbId`: ID en IMDb
- `imdbAverageRating`: Calificación promedio en IMDb
- `imdbNumVotes`: Número de votos en IMDb
- `availableCountries`: Países donde está disponible

Fuente: [datos.transporte.gob.ar](https://datos.transporte.gob.ar/)

## Requisitos

- Python 3.x
- pandas
- plotly
- nbformat (recomendado para visualización interactiva)

Instala las dependencias con:
```bash
pip install pandas plotly nbformat
```

## Ejecución

Ejecuta el programa principal desde la terminal:
```bash
python main.py
```

Los gráficos se abrirán automáticamente en tu navegador web. Si esto no ocurre, asegúrate de tener configurado el renderer de Plotly en modo `"browser"` (esto ya está implementado en el código).

## Visualizaciones Generadas
- **Cantidad de títulos por año de lanzamiento**: Gráfico de barras con la cantidad de títulos lanzados cada año.
- **Distribución de ratings según gémero**: Gráfico que muestra cómo se distribuyen los ratings de IMDb para cada género.
- **Cantidad de películas vs series**: Muestra la proporción de películas y series en el catálogo.

- **Calificación promedio de IMDb por género**: Compara el rating promedio de IMDb entre géneros principales.

## Ejemplo de uso

Al ejecutar el programa, se abrirán automáticamente gráficos interactivos en tu navegador, permitiendo explorar los datos de manera visual e intuitiva.

## Notas

- Asegúrate de tener el archivo `data.csv` en la misma carpeta que el resto de los scripts.
- Si tienes problemas para visualizar los gráficos, revisa que tu navegador predeterminado esté correctamente configurado.

## Autores

Gutierrez, Cesar 
Lopez, Micaela
Tagliaferro, Sabrina 
Zárate, Nahuel

## Licencia

Este proyecto es de uso académico y educativo.
