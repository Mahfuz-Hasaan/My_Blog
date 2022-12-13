from django.urls import path
from App_Login import views
app_name = 'App_Login'
urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout')
]
