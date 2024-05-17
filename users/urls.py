from django.urls import path

from users.views import register_view, login_view, confirmation_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('confirm/', confirmation_view, name='confirm'),
    path('logout/', login_view, name='logout')
]
