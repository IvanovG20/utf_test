from django.urls import path

from api.views import FoodAPIView


urlpatterns = [
    path('v1/foods/', FoodAPIView.as_view())
]
