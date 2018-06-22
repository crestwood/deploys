from django.conf.urls import url
from . import views           # This line is new!This explicitly imports views.py in the current folder.
urlpatterns = [
    url(r'^$', views.index),


    
    
]