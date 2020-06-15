from django.views.generic import ListView,DetailView
from .models import Movies

class MoviesListView(ListView):
    paginate_by = 15
    model = Movies

class MovieDetailView(DetailView):
    model = Movies