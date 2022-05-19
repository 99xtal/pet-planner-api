from django.urls import path
from meals import views

urlpatterns = [
    path('', views.MealList.as_view()),
    path('<int:pk>/', views.MealDetail.as_view()),
    path('foods/', views.FoodList.as_view()),
    path('foods/<int:pk>/', views.FoodDetail.as_view())
]