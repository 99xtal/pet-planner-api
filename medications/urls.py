from django.urls import path
from medications import views

urlpatterns = [
    path('', views.MedicationList.as_view()),
    path('<int:pk>/', views.MedicationDetail.as_view()),
    path('medicines/', views.MedicineList.as_view()),
    path('medicines/<int:pk>/', views.MedicineDetail.as_view())
]