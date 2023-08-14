from django.urls import path
from . import views
from wqpred.dash_apps.finished_apps import simpleexample


urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("result/<str:pk>", views.ResultView.as_view(), name='pred-result')
]