from django.urls import path
from .views import (
    AccountView,
    AccountCreate,
    AccountUpdate,
    AccountDelete,
    AccountLogin,
    AccountLogout,
)

app_name = 'accounts'
urlpatterns = [
    path('login/', AccountLogin.as_view(), name='account_login'),
    path('logout/', AccountLogout.as_view(), name='account_logout'),
    path('register/', AccountCreate.as_view(), name='account_create'),
    path('<str:username>/', AccountView.as_view(), name='account_current'),
    # path('<int:pk>/update/', AccountUpdate.as_view(), name='account_update'),
    # path('<int:pk>/delete/', AccountDelete.as_view(), name='account_delete'),
]