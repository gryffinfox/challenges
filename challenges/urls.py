from django.urls import path

from . import views

urlpatterns = [
    # path("challenges", views.challenges) would send us to challenges/challenges
    path("", views.index, name="index"),
    # month value is integer
    path("<int:month>", views.monthly_challenge_by_number),
    # month value is string
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
