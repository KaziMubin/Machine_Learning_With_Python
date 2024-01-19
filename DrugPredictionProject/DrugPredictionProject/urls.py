from django.contrib import admin
from django.urls import path
from DecisionTreeApp.views import IndexView, DataforPrediction


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view()),
    path("predict/", DataforPrediction.as_view())
]
