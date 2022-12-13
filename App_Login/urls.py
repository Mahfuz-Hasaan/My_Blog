from django.urls import path
from App_Login import views
app_name = 'App_Login'
urlpatterns = [
    path('signup/',views.SignUp,name='signup')
]
