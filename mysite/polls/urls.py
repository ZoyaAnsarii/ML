from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='poll_index'),
    path("about/",views.about, name='poll_about'),
]