from django.urls import path
from . import views
urlpatterns=[
    path('greetings/',view=views.grettings),
    path('register/',view=views.register)
    
]