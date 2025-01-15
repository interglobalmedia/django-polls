from django.urls import path

from . import views

app_name = "votes"

urlpatterns = [
    path("", views.VotesIndexView.as_view(), name="index"),
    path("<int:pk>/", views.VotesDetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.VotesResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
