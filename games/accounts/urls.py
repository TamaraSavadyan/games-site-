from django.urls import path
from .views import (
    AccountView,
    AccountCreate,
    AccountUpdate,
    AccountDelete
)

app_name = 'accounts'
urlpatterns = [
    path('', AccountView.as_view(), name='current_account'),
    path('register/', AccountCreate.as_view(), name='account_create'),
    path('<int:pk>/update/', AccountUpdate.as_view(), name='account_update'),
    path('<int:pk>/delete/', AccountDelete.as_view(), name='account_delete'),
]