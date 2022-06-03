from django.urls import path
from .views import Wordle

app_name = 'wordle'
urlpatterns = [
    path('wordle/', Wordle.as_view(), name='wordle_page'),

]