"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from games.views import (
    HomeView, 
    SuccessView,
    Error404View 
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='base'),
    path('home/', HomeView.as_view(), name='home'),
    path('success/', SuccessView.as_view(), name='success_page'),
    path('404-page/', Error404View.as_view(), name='404_page'),

    path('account/', include('accounts.urls'), name='accounts'),
    path('game-wordle/', include('wordle.urls'), name='game_wordle'),
    path('game-minesweeper/', include('minesweeper.urls'), name='game_minesweeper'),
    path('game-sudoku/', include('sudoku.urls'), name='game_sudoku'),

    path('admin/', admin.site.urls, name='admin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
