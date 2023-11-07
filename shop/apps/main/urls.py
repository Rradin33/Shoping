from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),         # yani boro az views, index mano run kon 
    path('sliders/', views.SliderView.as_view(), name='sliders'),
]


