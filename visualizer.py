# visualizer.py
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

class Visualizer:
    def __init__(self, renderer="browser", template="plotly_white"):
        self.renderer = renderer
        self.template = template

    def plot_titles_per_year(self, df, title="Cantidad de títulos por año", x_label="Año", y_label="Cantidad"):
        fig = px.line(df, x='releaseYear', y='count', title=title, template=self.template)
        fig.update_layout(
            xaxis_title=x_label,
            yaxis_title=y_label,
            font=dict(size=16, family="Arial"),
            title_font=dict(size=22, family="Arial Black"),
            plot_bgcolor="#fffaf6",
            yaxis=dict(gridcolor='#cccccc')
        )
        fig.update_traces(line=dict(width=3)) # Add this line to make the line thicker
        fig.show(renderer=self.renderer)

    def plot_avg_rating_by_genre(self, df, title="Promedio de rating por género", x_label="Género", y_label="Rating promedio"):
        fig = px.bar(df.sort_values(by='imdbAverageRating', ascending=False),
                     x='genres', y='imdbAverageRating', title=title, template=self.template,
                     color='imdbAverageRating', color_continuous_scale='Viridis')
        fig.update_layout(
            xaxis_title=x_label,
            yaxis_title=y_label,
            font=dict(size=16, family="Arial"),
            title_font=dict(size=22, family="Arial Black"),
            plot_bgcolor="#e5fcff",
            xaxis_tickangle=-45,
            coloraxis_showscale=True,
            coloraxis_colorbar=dict(title="Rating Promedio")
        )
        fig.show(renderer=self.renderer)

    def plot_type_distribution(self, df, title="Distribución por tipo de contenido"):
        fig = px.pie(df, values='count', names='type', title=title, template=self.template,
                     color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='#000000', width=3)))
        fig.update_layout(
            font=dict(size=16, family="Arial"),
            title_font=dict(size=22, family="Arial Black"),
            margin=dict(l=50, r=50, t=50, b=50)
        )
        fig.show(renderer=self.renderer)

    def plot_rating_distribution(self, series, title="Distribución de ratings IMDB", x_label="Rating", y_label="Cantidad"):
        fig = px.histogram(series, nbins=20, title=title, template=self.template, color_discrete_sequence=['#9bdfff'])
        fig.update_layout(
            xaxis_title=x_label,
            yaxis_title=y_label,
            font=dict(size=16, family="Arial"),
            title_font=dict(size=22, family="Arial Black"),
            plot_bgcolor="#effbff",
            margin=dict(l=50, r=50, t=50, b=50),
            yaxis=dict(gridcolor='#cccccc')
        )
        fig.show(renderer=self.renderer)