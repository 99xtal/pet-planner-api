from django.urls import path, include
from pets import views

urlpatterns = [
    path('', views.UserPetList.as_view()),
    path('<int:pk>/', views.PetDetail.as_view()),
    path('breeds/', views.BreedList.as_view())
]