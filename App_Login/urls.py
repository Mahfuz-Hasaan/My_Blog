from django.urls import path
from App_Login import views
app_name = 'App_Login'
urlpatterns = [
    path('signup/',views.SignUp,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.user_profile,name='user_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('change_password',views.pass_change,name='change_passowrd'),
    path('add_profile_pic/',views.add_profile_pic,name='add_profile_pic'),
    path('change_profile_pic/',views.change_pro_pic,name='change_profile_pic')
    
]

