from django.urls import path
from .views import (
    AccountView,
    AccountLogin,
    AccountCreate,
    AccountUpdate,
    AccountDelete
)

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/', AccountView.as_view(), name='account_current'),
    path('login/', AccountLogin.as_view(), name='account_login'),
    path('register/', AccountCreate.as_view(), name='account_create'),
    path('<int:pk>/update/', AccountUpdate.as_view(), name='account_update'),
    path('<int:pk>/delete/', AccountDelete.as_view(), name='account_delete'),
]