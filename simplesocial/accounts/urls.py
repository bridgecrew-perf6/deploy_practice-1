from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # after LOGIN, the user is redirected to url defined by "LOGIN_REDIRECT_URL" in settings.py file
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
    
    # after LOGOUT, the user is redirected to the url defined by "LOGOUT_REDIRECT_URL" in settings.py file
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 

    path('signup/', views.SignUp.as_view(), name='signup')
]