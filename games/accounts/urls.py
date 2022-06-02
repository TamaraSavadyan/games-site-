from django.urls import path
from .views import (
    Success,
    AccountCreate,
    AccountUpdate,
    AccountDelete
)

app_name = 'accounts'
urlpatterns = [
    path('success/', Success.as_view(), name='success_page'),
    path('register/', AccountCreate.as_view(), name='account_create'),
    path('<int:pk>/update/', AccountUpdate.as_view(), name='account_update'),
    path('<int:pk>/delete/', AccountDelete.as_view(), name='account_delete'),
]