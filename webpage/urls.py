from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name='contact'),
    path("card_color/", views.card_color, name='card_color'),
    path("card/", views.cardPage, name='card'),
]