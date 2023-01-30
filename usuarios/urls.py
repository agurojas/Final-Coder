from django.urls import path
from usuarios.views import login_view, register, update_user, update_user_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view()),
    path('signup/', register, name = 'register'),
    path('update/', update_user, name = 'update_user'),
    path('update/profile/', update_user_profile, name = 'update_user_profile'),
]