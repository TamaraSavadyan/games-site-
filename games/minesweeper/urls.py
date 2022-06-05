from django.urls import path
from .views import MinesweeperView

app_name = 'minesweeper'
urlpatterns = [
    path('', MinesweeperView.as_view(), name='minesweeper')
]