from django.urls import path
from .views import (
    AccountCreate,
    AccountUpdate,
    AccountDelete
)

app_name = 'accounts'
urlpatterns = [
    path('account/register/', AccountCreate.as_view(), name='account_create'),
    path('account/<int:pk>/update/', AccountUpdate.as_view(), name='account_update'),
    path('account/<int:pk>/delete/', AccountDelete.as_view(), name='account_delete'),
]