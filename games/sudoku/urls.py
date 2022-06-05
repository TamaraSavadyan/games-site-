from django.urls import path
from .views import SudokuView

app_name = 'sudoku'
urlpatterns = [
    path('', SudokuView.as_view(), name='sudoku')
]