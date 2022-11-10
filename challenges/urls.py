from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # challenges/
    path("<int:month>", views.challenges_int),
    path("<str:month>", views.challenges_class, name="string_challenge"),

]
