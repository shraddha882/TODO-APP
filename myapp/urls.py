from django.contrib import admin
from django.urls import path
from myapp.views import home,login, signup, add_todo, signout, delete

urlpatterns = [
    path('',home, name='home'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),
    path('add/', add_todo),
    path('delete/<int:id>', delete),
    path('logout/', signout),
]
