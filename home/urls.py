from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("jokes/", views.jokes, name='jokes'),
    path("ranting/", views.ranting, name='ranting'),
    path("quotes/", views.quotes, name='quotes'),
    path("school/", views.school, name='school'),
    path("family/", views.family, name='family'),     
    path("goodNews/", views.goodNews, name='goodNews')
    
]