from django.urls import path
from .views import _registrationView , _loginView , _aboutView , _logoutView

# ending points for edu_platform
urlpatterns = [
    
    path('edu_platform', _aboutView , name= 'about'),
    path('edu_platform/register/', _registrationView , name= 'registration'),
    path('edu_platform/login/', _loginView , name= 'login'),
      
]
