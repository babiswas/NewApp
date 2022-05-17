from django.urls import path
from .views import SignUp
from .views import AppUsers

app = 'Formuser'

urlpatterns = [
    path('register/', SignUp.as_view(), name='register'),
    path('all_user/', AppUsers.as_view(), name='users'),
]
