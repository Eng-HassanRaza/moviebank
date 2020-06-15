from django.urls import path
from .views import MoviesListView,MovieDetailView

urlpatterns = [
    path('', MoviesListView.as_view(),name='movies-list'),
    path('<pk>/', MovieDetailView.as_view(),name='movie-detail'),
]
